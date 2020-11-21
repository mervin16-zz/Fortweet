import json


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

                # Output
                self.output_path = settings["output"]["data_path"]

                # Filters
                self.filters = settings["filters"]

            # Set instance to self
            TwitterSettings.__instance__ = self
        else:
            raise Exception("You cannot create another TwitterSettings class")

    @staticmethod
    def get_instance():
        # Singleton static assignment
        if not TwitterSettings.__instance__:
            TwitterSettings()
        return TwitterSettings.__instance__

