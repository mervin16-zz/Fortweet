from app.setup.database import db
from app.helpers.utils import hash


class AdminModel(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

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
        db.session.commit()

    def insert(self):
        admin = self.find_by_username(self.username)
        if admin is None:
            # Hash the password
            self.password = hash(self.password)
            # Add to DB
            db.session.add(self)
            db.session.commit()
            return True

        return False
