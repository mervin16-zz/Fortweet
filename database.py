import sqlite3
from sqlite3.dbapi2 import connect


class Database:

    _database_location = "data/fortweets.db"
    __instance__ = None

    def __init__(self):

        # Constructor
        if Database.__instance__ is None:
            self.connection = sqlite3.connect(Database._database_location)
            cursor = self.connection.cursor()

            # get the count of tables with the name
            cursor.execute(
                """ SELECT count(name) FROM sqlite_master WHERE type='table' AND name='fortweets' """
            )

            # create table
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS fortweets
                        (author text, message text, time text)"""
            )

            self.connection.commit()

            # Set instance to self
            Database.__instance__ = self
        else:
            raise Exception("You cannot create another Database Connection")

    @staticmethod
    def connect():
        # Singleton static assignment
        if not Database.__instance__:
            Database()
        return Database.__instance__

    def commit(self):
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

