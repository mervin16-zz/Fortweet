from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
import app.helpers.utils as utils
import app.messages.response_errors as Err
import app.messages.responses_success as Succ
import app.models.tweet as tweet
import app.models.enums as enums
import app.services.streamer as streamer_mod


class Tweets(Resource):

    # [POST] Post a tweet in database
    @jwt_required
    def post(self):
        # Get json body from post request
        body = request.get_json()

        # Verify body format
        try:
            # Checks data
            value = body["value_flag"]

            if value == "start_live_tweet_streaming":

                streamer = streamer_mod.StreamerInit()
                has_started = streamer.start()

                if not has_started:
                    return Err.ERROR_STREAM_RUNNING
            else:
                return Err.ERROR_FLAG_INCORRECT

        except Exception as e:
            return Err.ERROR_JSON_FORMAT_INCORRECT

        return Succ.SUCCESS_TWEETS_STARTED

    # [GET] Get all tweets from database
    def get(self, page):
        print(page)
        tweets = tweet.TweetModel.get_paginate(200, page)
        return Succ.SUCCESS_TWEETS_RETURNED(utils.tweets_to_list(tweets.items))


class TweetSearch(Resource):

    # [GET] Search tweets by keywords
    def get(self):
        tweets = tweet.TweetModel.search(
            request.args["query"], enums.TweetSearch.Message
        )
        return Succ.SUCCESS_TWEETS_RETURNED(utils.tweets_to_list(tweets))


class AuthorSearch(Resource):

    # [GET] Search author by keywords
    def get(self):
        tweets = tweet.TweetModel.search(
            request.args["query"], enums.TweetSearch.Author
        )
        return Succ.SUCCESS_TWEETS_RETURNED(utils.tweets_to_list(tweets))


class SourceSearch(Resource):

    # [GET] Search source by keywords
    def get(self):
        tweets = tweet.TweetModel.search(
            request.args["query"], enums.TweetSearch.Source
        )
        return Succ.SUCCESS_TWEETS_RETURNED(utils.tweets_to_list(tweets))


class DateSearch(Resource):

    # [GET] Search date by keywords
    def get(self):
        tweets = tweet.TweetModel.search(request.args["query"], enums.TweetSearch.Date)
        return Succ.SUCCESS_TWEETS_RETURNED(utils.tweets_to_list(tweets))


class LocationSearch(Resource):

    # [GET] Search location by keywords
    def get(self):
        tweets = tweet.TweetModel.search(
            request.args["query"], enums.TweetSearch.Location
        )
        return Succ.SUCCESS_TWEETS_RETURNED(utils.tweets_to_list(tweets))
