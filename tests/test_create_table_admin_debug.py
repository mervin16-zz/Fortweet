import sqlite3

_database_location = "tests/databases/debug.db"

_connection = sqlite3.connect(_database_location)

_cursor = _connection.cursor()

# create table if it doesn't exists
_cursor.execute(
    """CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL, 
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )"""
)

# Add an admin
admin = ("admin1", "admin@gmail.com", "adminpass")

# Build query
query = "INSERT INTO admins VALUES (NULL, ?, ?, ?)"

# Executre query
_cursor.execute(query, admin)

_connection.commit()

_connection.close()
