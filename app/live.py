from flask import Blueprint, render_template as HTML, redirect
from flask.helpers import url_for
import app.models.tweet as tweet_mod

live = Blueprint("live", __name__, static_folder="static", template_folder="templates")


######################################
############# Main Pages #############
######################################


@live.route("/live")
def live_view():
    return HTML("live/index.html", page="live")


@live.route("/all/<int:page_num>")
def all_tweets(page_num):
    tweets = tweet_mod.TweetModel.get_paginate(50, page_num)
    return HTML("live/all_tweets.html", page="all", tweets=tweets)


@live.route("/stats")
def statistics():
    return HTML("live/statistics.html", page="stats")


@live.route("/about")
def about():
    return HTML("live/about.html", page="about")


######################################
############ Redirections ############
######################################


@live.route("/all")
def all_tweets_redirect():
    return redirect(url_for("live.all_tweets", page_num=1))
