from flask import Flask, render_template, jsonify
import tweepy
from settings import TwitterSettings
from services import sqliteServices
import sqlite3

app = Flask(__name__)

class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        sqliteServices.sqliteService.insert(status.text, status.created_at)
        out = f"{status.user.name} has tweeted -> {status.text}"
        print(out)

@app.route("/")
def index():

    # Get settings instance
    settings = TwitterSettings.get_instance()

    # Auths
    auth = tweepy.OAuthHandler(settings.consumer_key, settings.consumer_secret,)
    auth.set_access_token(
        settings.access_token, settings.access_token_secret,
    )

    # Get API
    api = tweepy.API(auth)

    # search = request.args.get("q")

    # public_tweets = api.user_timeline(search)

    # Live Tweets Streaming
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=["fortnite"])

    return jsonify(myStream)
    # return render_template("Filtering")


if __name__ == "__main__":
    app.run(debug=True)

