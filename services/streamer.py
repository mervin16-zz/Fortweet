import time
import tweepy
from setup.database import Database


class FStreamListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit

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

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create insert query
            query = "INSERT INTO fortweets VALUES (?, ?, ?, ?, ?, ?)"

            # Execute teh query
            cursor.execute(query, forttweet)

            # Commit Changes
            connection.commit()

            return True
        else:
            # Stop the loop of streaming
            return False

    def on_error(self, status):
        raise Exception(f"An error occurred while fetching tweets: {status}")
