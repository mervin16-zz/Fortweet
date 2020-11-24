import sqlite3


class Database:

    _database_location = "databases/tweety.db"
    __instance__ = None

    def __init__(self):
        raise Exception("You cannot create another Database Connection")

    @staticmethod
    def connect():
        return sqlite3.connect(Database._database_location)
