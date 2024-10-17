import sqlite3

class DataBase:
    def connect(self):
        try:
            self.con = sqlite3.connect('dataBase.db')
            self.cur = self.con.cursor()
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    # Procesar consulta SQL
    def SQL(self, query, params=()):
        try:
            self.cur.execute(query, params)
            if query.startswith('SELECT'):
                columns = [column[0] for column in self.cur.description]
                result = [dict(zip(columns, row)) for row in self.cur.fetchall()]
                return result
            self.con.commit()
        except sqlite3.Error as e:
            print(f"Error executing query: {e}")

    def close(self):
        try:
            self.con.close()
        except sqlite3.Error as e:
            print(f"Error closing the connection: {e}")


# Este módulo es un puente de conexión con la base de datos
# Se encarga de simpificar el proceso de conexión y consultas, manejando posibles errores en el proceso

# Junto a la clase CRUDModel de ./models/crud podrían usarse como componentes de un ORM sencillo