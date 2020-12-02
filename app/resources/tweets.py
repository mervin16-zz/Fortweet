from flask_restful import Resource, request
from flask_jwt_extended import jwt_required
from app.helpers.utils import tweets_to_list as Transform
from app.messages import response_errors as Err, responses_success as Succ
from app.models.tweet import TweetModel
from app.models.enums import TweetSearch as SearchEnum
from app.services.streamer import StreamerInit


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

                streamer = StreamerInit()
                has_started = streamer.start()

                if not has_started:
                    return Err.ERROR_STREAM_RUNNING
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
