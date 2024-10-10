import sqlite3

class dataBase:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def SQL(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def close(self):
        self.connection.close()