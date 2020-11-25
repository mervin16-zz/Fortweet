from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.tweets import (
    Tweets,
    TweetSearch,
    AuthorSearch,
    DateSearch,
    LocationSearch,
    SourceSearch,
)
from resources.admin import AdminLogin, AdminManage
from services.security import authenticate, identity
from messages import response_errors as Err
from setup.settings import TwitterSettings
from setup.database import db
from models.admin import AdminModel

# Create a Flask Application
app = Flask(__name__)

# Flask configurations
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///databases/fortweets.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True
app.secret_key = TwitterSettings.get_instance().jwt_secret_key
api = Api(app)

# SQLAlchemy configurations
db.app = app
db.init_app(app)
db.create_all()

# JWT Configurations
jwt = JWT(app, authenticate, identity)

# Creates default admins and insert in db
for admin in TwitterSettings.get_instance().super_admins:
    admin = AdminModel(admin["email"], admin["username"], admin["password"])
    db.session.add(admin)
    db.session.commit()

# Error handlers
@app.errorhandler(404)  # Handling HTTP 404 NOT FOUND
def page_not_found(e):
    return Err.ERROR_NOT_FOUND


# API Routes
api.add_resource(Tweets, "/api/tweets")
api.add_resource(TweetSearch, "/api/tweets/tweet")
api.add_resource(SourceSearch, "/api/tweets/source")
api.add_resource(AuthorSearch, "/api/tweets/author")
api.add_resource(DateSearch, "/api/tweets/date")
api.add_resource(LocationSearch, "/api/tweets/location")

api.add_resource(AdminLogin, "/admin/login")
api.add_resource(AdminManage, "/admin/manage")

# Start the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

