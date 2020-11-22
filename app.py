from flask import Flask
from flask_restful import Api
from settings import TwitterSettings
from database import Database
from tweets import Tweets
import threading as Corou
import time
import tweepy

# Create a Flask Application
app = Flask(__name__)
# Pass application to Api object
api = Api(app)

# API Routes
api.add_resource(Tweets, "/api/tweets")

if __name__ == "__main__":
    app.run(debug=True)

