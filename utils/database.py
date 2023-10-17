import sqlite3


class Database:
    def __init__(self, name):
        self.conn = sqlite3.connect(name, check_same_thread=False)
        self.cursor = self.conn.cursor()

    def init(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(id integer primary key AUTOINCREMENT,
                                         username TEXT not null,
                                         password TEXT not null,
                                         role TEXT not null,
                                         age INT) 
        """)
        # self.conn.close()


    def get_cursor(self):
        return self.conn.cursor()