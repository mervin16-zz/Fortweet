from admin import Admin

# TODO (Replace static admins to users in database)
admins = [Admin(1, "mervin", "1234")]

username_mapping = {u.username: u for u in admins}

id_mapping = {u.id: u for u in admins}


def authenticate(username, password):
    admin = username_mapping.get(username, None)

    if admin and admin.password == password:
        return admin


def identity(payload):
    admin_id = payload["identity"]
    return id_mapping.get(admin_id, None)
