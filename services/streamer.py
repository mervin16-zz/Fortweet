import time
import tweepy
from setup.database import Database
from setup.settings import TwitterSettings


class FStreamListener(tweepy.StreamListener):
    def __init__(self):
        self.start_time = time.time()
        self.limit = TwitterSettings.get_instance().stream_time

        # Get db connection
        self.connection = Database.connect()

        super(FStreamListener, self).__init__()

    def on_status(self, status):
        if (time.time() - self.start_time) < self.limit:

            # Create tweet object
            forttweet = (
                status.source,
                status.user.name,
                status.user.profile_background_image_url_https,
                status.text,
                status.created_at,
                status.user.location,
            )

            # Get the cursor
            cursor = self.connection.cursor()

            # Create insert query
            query = "INSERT INTO fortweets VALUES (?, ?, ?, ?, ?, ?)"

            # Execute teh query
            cursor.execute(query, forttweet)

            # Commit Changes
            self.connection.commit()

            return True
        else:
            # TODO Use Logger instead
            print("Live capture has stopped")

            # Close the DB connection
            self.connection.close()

            # Stop the loop of streaming
            return False

    def on_error(self, status):
        raise Exception(f"An error occurred while fetching tweets: {status}")
