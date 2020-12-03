import app.setup.database as database
import app.helpers.utils as utils


class AdminModel(database.db.Model):
    __tablename__ = "admins"

    id = database.db.Column(database.db.Integer, primary_key=True)
    email = database.db.Column(database.db.String(80))
    username = database.db.Column(database.db.String(80))
    password = database.db.Column(database.db.String(80))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        return AdminModel.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return AdminModel.query.filter_by(id=_id).first()

    @staticmethod
    def get_all():
        return AdminModel.query.all()

    @classmethod
    def remove(cls, id):
        AdminModel.query.filter_by(id=id).delete()
        database.db.session.commit()

    def insert(self):
        admin = self.find_by_username(self.username)
        if admin is None:
            # Hash the password
            self.password = utils.hash(self.password)
            # Add to DB
            database.db.session.add(self)
            database.db.session.commit()
            return True

        return False
