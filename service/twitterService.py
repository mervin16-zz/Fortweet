import time
import tweepy
from  setup import settings
from service import databaseService
from resources import errors

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=20):
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

            if (forttweet.count > 0):
                databaseService.insertLiveTweets(forttweet)

            return True
        else:
            # Stop the loop of streaming
            return False

    def on_error(self, status):
        raise errors.InternalServerError


def twitter_instantiation():
    # Get settings instance
    _settings = settings.TwitterSettings.get_instance()

    # Auths
    auth = tweepy.OAuthHandler(_settings.consumer_key, _settings.consumer_secret,)
    auth.set_access_token(
        _settings.access_token, _settings.access_token_secret,
    )

    # Get API
    api = tweepy.API(auth)

    # Live Tweets Streaming
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=_settings.filters)