import sqlite3
from database import Database


class Tweet:

    DB_LOCATION = "/database/fortweets.sqlite"

    def __init__(self, author, message, time):
        self.author = author
        self.message = message
        self.time = time

    def add(self, database):
        forttweet = (self.author, self.message, self.time)

        insert_query = "INSERT INTO fortweets VALUES (?, ?, ?)"

        database.connection.cursor().execute(insert_query, forttweet)
