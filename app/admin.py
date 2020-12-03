from flask import Blueprint, render_template as HTML, request
import app.models.admin as admin_mod
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

    return HTML(
        "admin/admins.html", admin_remove=True, admins=admin_mod.AdminModel.get_all()
    )


@admin.route("/add")
def admin_add_get():
    return HTML("admin/admin_add.html", error_message=None)


@admin.route("/add", methods=["POST"])
def admin_add_post():
    admin = admin_mod.AdminModel(
        request.form["admin-email"],
        request.form["admin-username"],
        request.form["admin-password"],
    )
    is_success = admin.insert()

    if is_success:
        return HTML(
            "admin/admins.html", admin_added=True, admins=admin_mod.AdminModel.get_all()
        )
    else:
        return HTML(
            "admin/admin_add.html",
            error_message=f"The admin {admin.username} already exists",
        )


@admin.route("/startstream", methods=["POST"])
def admin_start_stream():
    stream = streamer_mod.StreamerInit()
    stream.start()

    return "", 204

