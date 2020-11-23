from databases import Database
from resources import errors
class databaseService():

    def insertLiveTweets (self, forttweet):
        try:
            connection = Database.connect()
            cursor = connection.cursor()
            insert_query = "INSERT INTO fortweets VALUES (?, ?, ?, ?, ?)"

            cursor.execute(insert_query, forttweet)

            # Commit Changes
            connection.commit()
        
        except Exception as e:
            raise errors.SchemaValidationError