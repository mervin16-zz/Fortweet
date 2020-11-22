from flask import Flask, render_template, jsonify
import tweepy
from settings import TwitterSettings
import threading as Corou
import time
from database import Database
from tweet import Tweet
import json

app = Flask(__name__)


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, output_path, time_limit=20):
        self.start_time = time.time()
        self.limit = time_limit
        self.database = Database.connect()

        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        if (time.time() - self.start_time) < self.limit:
            # Create tweet object
            tweet = Tweet(status.user.name, status.text, status.created_at)

            # Add tweet to database
            tweet.add(self.database)

            # Commit Changes
            self.database.commit()

            return True
        else:
            # Close database connection
            self.database.disconnect()

            # Stop the loop of streaming
            return False

    def on_error(self, status):
        raise Exception(f"An error occurred while fetching tweets: {status}")


def twitter_instantiation():
    # Get settings instance
    settings = TwitterSettings.get_instance()

    # Auths
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret,)
    auth.set_access_token(
        settings.access_token, settings.access_token_secret,
    )

    # Get API
    api = tweepy.API(auth)

    # Live Tweets Streaming
    myStreamListener = MyStreamListener(settings.output_path)
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["fortnite"])


@app.route("/")
def index():

    stream = Corou.Thread(target=twitter_instantiation)
    stream.start()

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)

