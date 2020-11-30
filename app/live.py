from flask import Blueprint, render_template as HTML

live = Blueprint("live", __name__, static_folder="static", template_folder="templates")


@live.route("/")
def live_view():
    return HTML("live/index.html")
