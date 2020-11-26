from setup.database import db


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

    def insert(self):
        admin = self.find_by_username(self.username)
        if admin is None:
            db.session.add(self)
            db.session.commit()
