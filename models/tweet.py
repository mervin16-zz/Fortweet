from setup.database import db


class TweetModel(db.Model):
    __tablename__ = "fortweets"

    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(80))
    author = db.Column(db.String(80))
    profile_pic = db.Column(db.String())
    message = db.Column(db.String())
    date = db.Column(db.String(80))
    location = db.Column(db.String(80))

    def __init__(self, source, author, profile_pic, message, date, location):
        self.source = source
        self.author = author
        self.profile_pic = profile_pic
        self.message = message
        self.date = date
        self.location = location

    def json(self):
        return {
            "source": self.source,
            "author": {"name": self.author, "profile": self.profile_pic,},
            "tweet": self.message,
            "time": self.date,
            "location": self.location,
        }

    def insert(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return TweetModel.query.all()

    @classmethod
    def search_by_message(cls, query):
        # Check if query is not none
        if query is not None:
            return TweetModel.query.filter(TweetModel.message.like(f"%{query}%")).all()

    @classmethod
    def search_by_author(cls, query):
        # Check if query is not none
        if query is not None:
            return TweetModel.query.filter(TweetModel.author.like(f"%{query}%")).all()

    @classmethod
    def search_by_source(cls, query):
        # Check if query is not none
        if query is not None:
            return TweetModel.query.filter(TweetModel.source.like(f"%{query}%")).all()

    @classmethod
    def search_by_date(cls, query):
        # Check if query is not none
        if query is not None:
            return TweetModel.query.filter(TweetModel.date.like(f"%{query}%")).all()

    @classmethod
    def search_by_location(cls, query):
        # Check if query is not none
        if query is not None:
            return TweetModel.query.filter(TweetModel.location.like(f"%{query}%")).all()
