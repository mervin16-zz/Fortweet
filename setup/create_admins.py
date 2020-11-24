from database import Database
from settings import TwitterSettings

#############################################################
########## Creates all necessary tables in project ##########
#############################################################

_connection = Database.connect()

_cursor = _connection.cursor()

for admin in TwitterSettings.get_instance().super_admins:

    # Add the default admin TODO(Improve this code)
    admin = (admin["username"], admin["email"], admin["password"])
    # Build query
    query = "INSERT INTO admins VALUES (NULL, ?, ?, ?)"
    # Executre query
    _cursor.execute(query, admin)

    _connection.commit()

_connection.close()
