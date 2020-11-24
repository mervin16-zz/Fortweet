from setup.database import Database


class AdminModel:
    __TABLE_NAME = "admins"

    def __init__(self, _id, email, username, password):
        self.id = _id
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = Database.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE username=?".format(table=cls.__TABLE_NAME)
        result = cursor.execute(query, (username,))
        row = result.fetchone()
        if row:
            admin = cls(*row)
        else:
            admin = None

        connection.close()
        return admin

    @classmethod
    def find_by_id(cls, _id):
        connection = Database.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM {table} WHERE id=?".format(table=cls.__TABLE_NAME)
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            admin = cls(*row)
        else:
            admin = None

        connection.close()
        return admin
