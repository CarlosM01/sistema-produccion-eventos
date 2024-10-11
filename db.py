import sqlite3

class DataBase:
    def connect(self):
        self.con = sqlite3.connect('dataBase.db')
        self.cur = self.con.cursor()

    def SQL(self, query, params=()):
        self.cur.execute(query, params)
        if query.strip().upper().startswith('SELECT'):
            result = self.cur.fetchall()
            return result
        self.con.commit()

    def close(self):
        self.con.close()