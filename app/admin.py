from flask import Blueprint, render_template as HTML, request, redirect
from flask.helpers import flash, url_for
import app.models.admin as admin_mod
import app.models.tweet as tweet_mod
import app.services.streamer as streamer_mod

admin = Blueprint(
    "admin", __name__, static_folder="static", template_folder="templates"
)


@admin.route("/dashboard")
def admin_dashboard():
    return HTML("admin/dashboard.html")


@admin.route("/analysis")
def admin_analysis():
    return HTML("admin/analysis.html")


@admin.route("/manage")
def admin_manage():
    return HTML("admin/admins.html", admins=admin_mod.AdminModel.get_all())


@admin.route("/settings")
def admin_settings():
    return HTML("admin/settings.html")


@admin.route("/remove/<id>", methods=["POST"])
def admin_delete(id):
    # Remove admin
    admin_mod.AdminModel.remove(id)

    flash(f"Admin removed", "error")

    return redirect(url_for("admin.admin_manage"))


@admin.route("/add")
def admin_add_get():
    return HTML("admin/admin_add.html")


@admin.route("/add", methods=["POST"])
def admin_add_post():
    admin = admin_mod.AdminModel(
        request.form["admin-email"],
        request.form["admin-username"],
        request.form["admin-password"],
    )
    is_success = admin.insert()

    if is_success:
        flash(f"The admin {admin.username} has been added", "success")
        return redirect(url_for("admin.admin_manage"))
    else:
        flash(f"The admin {admin.username} already exists", "error")
        return redirect(url_for("admin.admin_add_get"))


@admin.route("/deletetweets", methods=["POST"])
def admin_delete_tweets():
    # Delete all tweets
    tweet_mod.TweetModel.delete_all()

    flash("All tweets has been deleted", "error")

    return redirect(url_for("admin.admin_settings"))


@admin.route("/startstream", methods=["POST"])
def admin_start_stream():
    # Starts the streaming
    stream = streamer_mod.StreamerInit()
    stream.start()

    # Returns a no content status code
    # because the user doesn't need to get away
    # from current page
    return "", 204

