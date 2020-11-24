from setup.database import Database


class TweetModel:
    __TABLE_NAME = "fortweets"

    # Get all tweets from database
    @classmethod
    def get_all(cls):
        # Get db connection
        connection = Database.connect()

        # Get the cursor
        cursor = connection.cursor()

        # Create the query
        query = f"SELECT * FROM {cls.__TABLE_NAME}"

        # Execute the query
        results = cursor.execute(query)

        # Iterate through results
        # Also create a tweets list to append result
        tweets = []
        for row in results:
            tweets.append(
                {
                    "source": row[0],
                    "author": {"name": row[1], "profile": row[2],},
                    "tweet": row[3],
                    "time": row[4],
                    "location": row[5],
                }
            )

        connection.close()
        return tweets

    @classmethod
    def search_by_message(cls, query):
        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM {cls.__TABLE_NAME} WHERE message LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": {"name": row[1], "profile": row[2],},
                        "tweet": row[3],
                        "time": row[4],
                        "location": row[5],
                    }
                )
            connection.close()

            return tweets

    @classmethod
    def search_by_author(cls, query):
        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM {cls.__TABLE_NAME} WHERE author LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": {"name": row[1], "profile": row[2],},
                        "tweet": row[3],
                        "time": row[4],
                        "location": row[5],
                    }
                )
            connection.close()

            return tweets

    @classmethod
    def search_by_source(cls, query):
        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM {cls.__TABLE_NAME} WHERE source LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": {"name": row[1], "profile": row[2],},
                        "tweet": row[3],
                        "time": row[4],
                        "location": row[5],
                    }
                )
            connection.close()

            return tweets

    @classmethod
    def search_by_date(cls, query):
        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM {cls.__TABLE_NAME} WHERE time LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": {"name": row[1], "profile": row[2],},
                        "tweet": row[3],
                        "time": row[4],
                        "location": row[5],
                    }
                )
            connection.close()

            return tweets

    @classmethod
    def search_by_location(cls, query):
        # Check if query is not none
        if query is not None:

            # Get db connection
            connection = Database.connect()

            # Get the cursor
            cursor = connection.cursor()

            # Create the query
            query = f"SELECT * FROM {cls.__TABLE_NAME} WHERE location LIKE '%{query}%'"

            # Execute the query
            results = cursor.execute(query)

            # Iterate through results
            # Also create a tweets list to append result
            tweets = []
            for row in results:
                tweets.append(
                    {
                        "source": row[0],
                        "author": {"name": row[1], "profile": row[2],},
                        "tweet": row[3],
                        "time": row[4],
                        "location": row[5],
                    }
                )
            connection.close()

            return tweets
