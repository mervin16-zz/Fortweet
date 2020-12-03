from flask import Blueprint
from flask_restful import Api
import app.resources.tweets as tweets_mod
import app.resources.fortauth as fortauth

api_bp = Blueprint("api", __name__, static_folder="static", template_folder="templates")

api = Api(api_bp)

# API Routes
api.add_resource(tweets_mod.Tweets, "/tweets")
api.add_resource(tweets_mod.TweetSearch, "/tweets/tweet")
api.add_resource(tweets_mod.SourceSearch, "/tweets/source")
api.add_resource(tweets_mod.AuthorSearch, "/tweets/author")
api.add_resource(tweets_mod.DateSearch, "/tweets/date")
api.add_resource(tweets_mod.LocationSearch, "/tweets/location")
api.add_resource(fortauth.FortAuth, "/fortauth")
