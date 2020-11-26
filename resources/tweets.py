from flask_restful import Resource, request
from flask_jwt import jwt_required
from setup.settings import TwitterSettings
from services.streamer import FStreamListener
from messages import response_errors as Err, responses_success as Succ
from models.tweet import TweetModel
from models.enums import TweetSearch as SearchEnum
import threading as Coroutine
import tweepy
from helpers.utils import tweets_to_list as Transform


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
        myStreamListener = FStreamListener()
        myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
        myStream.filter(track=settings.filters)

    # [POST] Post a tweet in database
    @jwt_required()
    def post(self):
        # Get json body from post request
        body = request.get_json()

        # Verify body format
        try:
            # Checks data
            value = body["value_flag"]

            if value == "start_live_tweet_streaming":

                # TODO (Improve Threading)
                stream = Coroutine.Thread(target=self.__twitterInstantiation)
                stream.start()
                stream.join()

            else:
                return Err.ERROR_FLAG_INCORRECT

        except Exception as e:
            return Err.ERROR_JSON_FORMAT_INCORRECT

        return Succ.SUCCESS_TWEETS_STARTED

    # [GET] Get all tweets from database
    def get(self):
        tweets = TweetModel.get_all()
        return Succ.SUCCESS_TWEETS_RETURNED(Transform(tweets))


class TweetSearch(Resource):

    # [GET] Search tweets by keywords
    def get(self):
        tweets = TweetModel.search(request.args["query"], SearchEnum.Message)
        return Succ.SUCCESS_TWEETS_RETURNED(Transform(tweets))


class AuthorSearch(Resource):

    # [GET] Search author by keywords
    def get(self):
        tweets = TweetModel.search(request.args["query"], SearchEnum.Author)
        return Succ.SUCCESS_TWEETS_RETURNED(Transform(tweets))


class SourceSearch(Resource):

    # [GET] Search source by keywords
    def get(self):
        tweets = TweetModel.search(request.args["query"], SearchEnum.Source)
        return Succ.SUCCESS_TWEETS_RETURNED(Transform(tweets))


class DateSearch(Resource):

    # [GET] Search date by keywords
    def get(self):
        tweets = TweetModel.search(request.args["query"], SearchEnum.Date)
        return Succ.SUCCESS_TWEETS_RETURNED(Transform(tweets))


class LocationSearch(Resource):

    # [GET] Search location by keywords
    def get(self):
        tweets = TweetModel.search(request.args["query"], SearchEnum.Location)
        return Succ.SUCCESS_TWEETS_RETURNED(Transform(tweets))
