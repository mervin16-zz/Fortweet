from flask import Blueprint, render_template as HTML
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
    print(f"Admin with ID {id} has been deleted")
    return HTML("admin/admins.html", admin_remove=True, admins=AdminModel.get_all())


@admin.route("/add", methods=["GET"])
def admin_add_get():
    return HTML("admin/admin_add.html")


@admin.route("/add", methods=["POST"])
def admin_add_post():
    print(f"Admin has been added")
    return HTML("admin/admins.html", admin_added=True, admins=AdminModel.get_all())
