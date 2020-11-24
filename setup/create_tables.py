from database import Database

#############################################################
########## Creates all necessary tables in project ##########
#############################################################

_connection = Database.connect()

_cursor = _connection.cursor()

# Create the table Admins
_cursor.execute(
    """CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL, 
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )"""
)

# Create the table Fortweets
_cursor.execute(
    """CREATE TABLE IF NOT EXISTS tweets (
        source TEXT,
        author TEXT NOT NULL, 
        author_pic_url,
        message TEXT NOT NULL, 
        time TEXT NOT NULL,
        location TEXT
    )"""
)

# Add the default admin TODO(Improve this code)
admin = ("th3pl4gu3", "th3pl4gu33@gmail.com", "th3pl4gu3")
# Build query
query = "INSERT INTO admins VALUES (NULL, ?, ?, ?)"
# Executre query
_cursor.execute(query, admin)

_connection.commit()

_connection.close()
