import sqlite3

class DatabaseMange:
    def __init__(self, dbname):
        conn = sqlite3.connect(dbname)
        cur = conn.cursor()

    def __del__(self):
        conn.close