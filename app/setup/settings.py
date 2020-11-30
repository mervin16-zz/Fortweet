import json
from app.services.logger import get_logger as Logger


class TwitterSettings:
    __instance__ = None

    def __init__(self):

        # Constructor
        if TwitterSettings.__instance__ is None:

            # Fetch settings from json file
            with open("config/settings.json") as json_file:
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

                # Database
                self.database_path = settings["database"]["path"]

            # Set instance to self
            TwitterSettings.__instance__ = self
        else:
            Logger().debug("Exception occured with TwitterSettings class instantiation")
            raise Exception("You cannot create another TwitterSettings class")

    @staticmethod
    def get_instance():
        # Singleton static assignment
        if not TwitterSettings.__instance__:
            TwitterSettings()
        return TwitterSettings.__instance__

