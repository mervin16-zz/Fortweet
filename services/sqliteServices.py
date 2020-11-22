import sqlite3

class sqliteService():
    def insert(self, status):
        conn = sqlite3.connect('C:\\sqlite3\\myTweet.db')
        c = conn.cursor()
        c.execute("""INSERT INTO tweets (text,created_at) VALUES(?,?)""",
          (status.text, status.created_at))
        conn.commit()