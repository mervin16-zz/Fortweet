import app.setup.database as database
import app.models.enums as enums
import app.services.logger as logger


class TweetModel(database.db.Model):
    __tablename__ = "fortweets"

    id = database.db.Column(database.db.Integer, primary_key=True)
    source = database.db.Column(database.db.String(80))
    author = database.db.Column(database.db.String(80))
    profile_pic = database.db.Column(database.db.String())
    message = database.db.Column(database.db.String())
    date = database.db.Column(database.db.String(80))
    location = database.db.Column(database.db.String(80))

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
        database.db.session.add(self)
        database.db.session.commit()

    @staticmethod
    def get_all():
        return TweetModel.query.all()

    @staticmethod
    def search(query, search_enum):

        # Check if query is not none
        if query is not None:

            if search_enum == enums.TweetSearch.Message:
                filter = TweetModel.message.like(f"%{query}%")
            elif search_enum == enums.TweetSearch.Author:
                filter = TweetModel.author.like(f"%{query}%")
            elif search_enum == enums.TweetSearch.Source:
                filter = TweetModel.source.like(f"%{query}%")
            elif search_enum == enums.TweetSearch.Date:
                filter = TweetModel.date.like(f"%{query}%")
            elif search_enum == enums.TweetSearch.Location:
                filter = TweetModel.location.like(f"%{query}%")
            else:
                logger.get_logger().debug(
                    "An internal error occurred while filtering data"
                )
                raise Exception("An internal error occured while filtering data.")

            return TweetModel.query.filter(filter).all()
