from flask import Blueprint, render_template as HTML, request
from app.models.admin import AdminModel

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
    return HTML("admin/admins.html", admins=AdminModel.get_all())


@admin.route("/settings")
def admin_settings():
    return HTML("admin/settings.html")


@admin.route("/remove/<id>", methods=["POST"])
def admin_delete(id):
    # Remove admin
    AdminModel.remove(id)

    return HTML("admin/admins.html", admin_remove=True, admins=AdminModel.get_all())


@admin.route("/add")
def admin_add_get():
    return HTML("admin/admin_add.html", error_message=None)


@admin.route("/add", methods=["POST"])
def admin_add_post():
    admin = AdminModel(
        request.form["admin-email"],
        request.form["admin-username"],
        request.form["admin-password"],
    )
    is_success = admin.insert()

    if is_success:
        return HTML("admin/admins.html", admin_added=True, admins=AdminModel.get_all())
    else:
        return HTML(
            "admin/admin_add.html",
            error_message=f"The admin {admin.username} already exists",
        )
