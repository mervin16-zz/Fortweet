from models.admin import AdminModel as Admin


def authenticate(username, password):
    admin = Admin.find_by_username(username)

    if admin and admin.password == password:
        return admin


def identity(payload):
    admin_id = payload["identity"]
    return Admin.find_by_id(admin_id)
