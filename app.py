from flask import Flask
from flask_restful import Api
from tweets import (
    Tweets,
    TweetSearch,
    AuthorSearch,
    DateSearch,
    LocationSearch,
    SourceSearch,
)

# Create a Flask Application
app = Flask(__name__)
# Pass application to Api object
api = Api(app)


# Error Handlers
@app.errorhandler(404)  # Handling HTTP 404 NOT FOUND
def page_not_found(e):
    return (
        {
            "tweets": [],
            "message": "No tweets found under this identifier.",
            "success": False,
        },
        404,
    )


# API Routes
api.add_resource(Tweets, "/api/tweets")
api.add_resource(TweetSearch, "/api/tweets/tweet/search")
api.add_resource(SourceSearch, "/api/tweets/source/search")
api.add_resource(AuthorSearch, "/api/tweets/author/search")
api.add_resource(DateSearch, "/api/tweets/date/search")
api.add_resource(LocationSearch, "/api/tweets/location/search")

if __name__ == "__main__":
    app.run(debug=True)

