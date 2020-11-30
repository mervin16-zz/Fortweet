from app.setup.database import db
from app.models.enums import TweetSearch
from app.services.logger import get_logger as Logger


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

    @staticmethod
    def get_all():
        return TweetModel.query.all()

    @staticmethod
    def search(query, search_enum):

        # Check if query is not none
        if query is not None:

            if search_enum == TweetSearch.Message:
                filter = TweetModel.message.like(f"%{query}%")
            elif search_enum == TweetSearch.Author:
                filter = TweetModel.author.like(f"%{query}%")
            elif search_enum == TweetSearch.Source:
                filter = TweetModel.source.like(f"%{query}%")
            elif search_enum == TweetSearch.Date:
                filter = TweetModel.date.like(f"%{query}%")
            elif search_enum == TweetSearch.Location:
                filter = TweetModel.location.like(f"%{query}%")
            else:
                Logger().debug("An internal error occurred while filtering data")
                raise Exception("An internal error occured while filtering data.")

            return TweetModel.query.filter(filter).all()
