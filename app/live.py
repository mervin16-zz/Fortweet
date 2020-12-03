from flask import Blueprint, render_template as HTML, redirect
from flask.helpers import url_for
import app.models.tweet as tweet_mod

live = Blueprint("live", __name__, static_folder="static", template_folder="templates")


@live.route("/live")
def live_view():
    return HTML("live/index.html")


@live.route("/all")
def all_tweets_redirect():
    return redirect(url_for("live.all_tweets", page_num=1))


@live.route("/all/<int:page_num>")
def all_tweets(page_num):
    tweets = tweet_mod.TweetModel.get_paginate(50, page_num)
    return HTML("live/all_tweets.html", tweets=tweets)
