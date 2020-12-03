import json
import os
import app.services.logger as logger


class TwitterSettings:
    __instance__ = None

    def __init__(self):

        # Constructor
        if TwitterSettings.__instance__ is None:

            # Checks if file exists
            # If not, use environment variables
            if os.path.isdir("app/config"):

                # Fetch settings from json file
                with open("app/config/settings.json") as json_file:
                    # Load settings
                    settings = json.load(json_file)

                    # API Settings
                    self.consumer_key = settings["api"]["consumer_key"]
                    self.consumer_secret = settings["api"]["consumer_secret"]
                    self.access_token = settings["api"]["access_token"]
                    self.access_token_secret = settings["api"]["access_token_secret"]

                    # Streaming
                    self.filters = settings["streaming"]["filters"]
                    self.stream_time = settings["streaming"]["stream_time"]

                    # Super Admins
                    self.super_admins = settings["super_admins"]

                    # Keys
                    self.jwt_secret_key = settings["key"]["jwt_secret"]

            else:
                # API Settings
                self.consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
                self.consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
                self.access_token = os.environ["TWITTER_ACCESS_TOKEN"]
                self.access_token_secret = os.environ["TWITTER_ACCESS_SECRET"]

                # Streaming
                self.filters = os.environ["FILTERS"]
                self.stream_time = os.environ["STREAM_TIME"]

                # Super Admins
                self.super_admins = os.environ["SUPER_ADMINS"]

                # Keys
                self.jwt_secret_key = os.environ["JWT_SECRET"]

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

