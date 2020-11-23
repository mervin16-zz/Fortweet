from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from core.tweets import (
    Tweets,
    TweetSearch,
    AuthorSearch,
    DateSearch,
    LocationSearch,
    SourceSearch,
)
from core.admin import Login, TokenManagement, AdminManage
from services.security import authenticate, identity
from messages import response_errors as Err

# Create a Flask Application
app = Flask(__name__)
# Set a secret key
app.secret_key = "mervin"  # TODO("Hide Secret Key")
app.config["PROPAGATE_EXCEPTIONS"] = True
# Pass application to Api object
api = Api(app)
# Initialize Jwt object
jwt = JWT(app, authenticate, identity)

# Error Handlers
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

api.add_resource(AdminManage, "/api/token")

api.add_resource(Login, "/admin/login")
api.add_resource(TokenManagement, "/admin/tokens")

if __name__ == "__main__":
    app.run(debug=True)

