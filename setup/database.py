import sqlite3


class Database:

    _database_location = "databases/fortweets.db"
    __instance__ = None

    def __init__(self):
        raise Exception("You cannot create another Database Connection")

    @staticmethod
    def connect():
        connection = sqlite3.connect(Database._database_location)
        cursor = connection.cursor()

        # create table if it doesn't exists
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS fortweets (
                source TEXT,
                author TEXT NOT NULL, 
                author_pic_url,
                message TEXT NOT NULL, 
                time TEXT NOT NULL,
                location TEXT
            )"""
        )

        connection.commit()

        return connection

