from flask_restful import Resource, request
from database import Database
from settings import TwitterSettings
import threading as Coroutine
import tweepy
import time


class MyStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit

        super(MyStreamListener, self).__init__()

    def on_status(self, status):
        if (time.time() - self.start_time) < self.limit:

            # Create tweet object
            forttweet = (
                status.source,
                status.user.name,
                status.text,
                status.created_at,
                status.user.location,
            )

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create insert query
            query = "INSERT INTO fortweets VALUES (?, ?, ?, ?, ?)"

            # Execute teh query
            cursor.execute(query, forttweet)

            # Commit Changes
            connection.commit()

            return True
        else:
            # Stop the loop of streaming
            return False

    def on_error(self, status):
        raise Exception(f"An error occurred while fetching tweets: {status}")


class Tweets(Resource):

    # [Private] Twitter configurations
    def __twitterInstantiation(self):
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
        myStreamListener = MyStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(track=settings.filters)

    # [POST] Post a tweet in database
    def post(self):
        # Get json body from post request
        body = request.get_json()

        # Verify body format
        try:
            # Checks data
            value = body["value_flag"]

            if value == "start_live_tweet_streaming":
                stream = Coroutine.Thread(target=self.__twitterInstantiation)
                stream.start()
            else:
                return ({"message": "Incorrect flag sent", "success": False}, 400)

        except Exception as e:
            return ({"message": "Incorrect JSON format", "success": False}, 400)

        return ({"message": "Live tweets capturing has started", "success": True}, 200)

    # [GET] Get all tweets from database
    def get(self):
        # Get db connection
        connection = Database.connect()

        # Get the cursor
        cursor = connection.cursor()

        # Create the query
        query = "SELECT * FROM fortweets"

        # Execute the query
        results = cursor.execute(query)

        # Iterate through results
        # Also create a tweets list to append result
        tweets = []
        for row in results:
            tweets.append(
                {
                    "source": row[0],
                    "author": row[1],
                    "tweet": row[2],
                    "time": row[3],
                    "location": row[4],
                }
            )

        connection.close()

        return ({"tweets": tweets, "message": "", "success": True,}, 200)


class TweetSearch(Resource):

    # [GET] Search tweets by keywords
    def get(self):
        # Get the query
        query = request.args["query"]

        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM fortweets WHERE message LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": row[1],
                        "tweet": row[2],
                        "time": row[3],
                        "location": row[4],
                    }
                )

            connection.close()

            return ({"tweets": tweets, "message": "", "success": True,}, 200)


class AuthorSearch(Resource):

    # [GET] Search author by keywords
    def get(self):
        # Get the query
        query = request.args["query"]

        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM fortweets WHERE author LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": row[1],
                        "tweet": row[2],
                        "time": row[3],
                        "location": row[4],
                    }
                )

            connection.close()

            return ({"tweets": tweets, "message": "", "success": True,}, 200)


class SourceSearch(Resource):

    # [GET] Search source by keywords
    def get(self):
        # Get the query
        query = request.args["query"]

        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM fortweets WHERE source LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": row[1],
                        "tweet": row[2],
                        "time": row[3],
                        "location": row[4],
                    }
                )

            connection.close()

            return ({"tweets": tweets, "message": "", "success": True,}, 200)


class DateSearch(Resource):

    # [GET] Search date by keywords
    def get(self):
        # Get the query
        query = request.args["query"]

        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM fortweets WHERE author time '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": row[1],
                        "tweet": row[2],
                        "time": row[3],
                        "location": row[4],
                    }
                )

            connection.close()

            return ({"tweets": tweets, "message": "", "success": True,}, 200)


class LocationSearch(Resource):

    # [GET] Search location by keywords
    def get(self):
        # Get the query
        query = request.args["query"]

        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM fortweets WHERE location LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": row[1],
                        "tweet": row[2],
                        "time": row[3],
                        "location": row[4],
                    }
                )

            connection.close()

            return ({"tweets": tweets, "message": "", "success": True,}, 200)
