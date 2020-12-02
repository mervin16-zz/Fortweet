import time
import tweepy
import threading as Coroutine
from app import socketio
from app.messages import constants as Const
from app.setup.settings import TwitterSettings
from app.models.tweet import TweetModel
from app.services.logger import get_logger as Logger


class FStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.start_time = time.time()
        self.limit = TwitterSettings.get_instance().stream_time

        Logger().debug("Live capture has started")

        # Notify client that a live capture will start
        socketio.emit(
            "stream-started", True, broadcast=True,
        )

        super(FStreamListener, self).__init__()

    def on_status(self, status):
        if (time.time() - self.start_time) < self.limit:

            # Create tweet object
            forttweet = TweetModel(
                status.source,
                status.user.name,
                status.user.profile_background_image_url_https,
                status.text,
                status.created_at,
                status.user.location,
            )

            # Emit to socket
            socketio.emit(
                "stream-results",
                {
                    "profile_pic": forttweet.profile_pic,
                    "author": forttweet.author,
                    "message": forttweet.message,
                },
                broadcast=True,
            )

            # Add to database
            forttweet.insert()

            return True
        else:
            Logger().debug("Live capture has ended")

            # Notify client that a live capture has ended
            socketio.emit(
                "stream-ended", True, broadcast=True,
            )

            # Stop the loop of streaming
            return False

    def on_error(self, status):
        Logger().debug(f"An error occurred while fetching tweets: {status}")
        raise Exception(f"An error occurred while fetching tweets: {status}")


class StreamerInit:

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

    def start(self):
        for coro in Coroutine.enumerate():
            if coro.name == Const.FLAG_TWEETS_LIVE_CAPTURE:
                return False

        stream = Coroutine.Thread(target=self.__twitterInstantiation)
        stream.setName(Const.FLAG_TWEETS_LIVE_CAPTURE)
        stream.start()

        return True
