import time
import tweepy
import threading as Coroutine
import app.messages.constants as Const
import app.setup.settings as settings_mod
import app.models.tweet as tweet_mod
import app.services.logger as logger
import app


class FStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.start_time = time.time()
        self.limit = settings_mod.TwitterSettings.get_instance().stream_time

        logger.get_logger().debug("Live capture has started")

        # Notify client that a live capture will start
        app.socketio.emit(
            "stream-started", True, broadcast=True,
        )

        super(FStreamListener, self).__init__()

    def on_status(self, status):
        if (time.time() - self.start_time) < self.limit:

            # Create tweet object
            forttweet = tweet_mod.TweetModel(
                status.source,
                status.user.name,
                status.user.profile_background_image_url_https,
                status.text,
                status.created_at,
                status.user.location,
            )

            # Emit to socket
            app.socketio.emit(
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
            logger.get_logger().debug("Live capture has ended")

            # Notify client that a live capture has ended
            app.socketio.emit(
                "stream-ended", True, broadcast=True,
            )

            # Stop the loop of streaming
            return False

    def on_error(self, status):
        logger.get_logger().debug(f"An error occurred while fetching tweets: {status}")
        raise Exception(f"An error occurred while fetching tweets: {status}")


class StreamerInit:

    # [Private] Twitter configurations
    def __twitterInstantiation(self):
        # Get settings instance
        settings = settings_mod.TwitterSettings.get_instance()
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
