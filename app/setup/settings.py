import os
import app.services.logger as logger


class TwitterSettings:
    __instance__ = None

    def __init__(self):

        # Constructor
        if TwitterSettings.__instance__ is None:

            # API Settings
            self.consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
            self.consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
            self.access_token = os.environ["TWITTER_ACCESS_TOKEN"]
            self.access_token_secret = os.environ["TWITTER_ACCESS_SECRET"]

            # Streaming
            self.filters = os.environ["FILTERS"].split(",")
            self.stream_time = float(os.environ["STREAM_TIME"])

            # Super Admins
            self.super_admin = os.environ["SUPER_ADMINS"].split(",")

            # Keys
            self.jwt_secret_key = os.environ["JWT_SECRET"]

            # Db Settings
            self.db_name = os.environ["DB_NAME"]
            self.db_host = os.environ["DB_HOST"]
            self.db_username = os.environ["DB_USERNAME"]
            self.db_password = os.environ["DB_PASSWORD"]

            # Set instance to self
            TwitterSettings.__instance__ = self
        else:
            logger.get_logger().debug(
                "Exception occured with TwitterSettings class instantiation"
            )
            raise Exception("You cannot create another TwitterSettings class")

    @staticmethod
    def get_instance():
        # Singleton static assignment
        if not TwitterSettings.__instance__:
            TwitterSettings()
        return TwitterSettings.__instance__

