import sqlite3            #Importa el método "sqlite3".

class DataBase:           #Define la clase "DataBase" que encapsula la lógica para gestionar una base de datos SQLite.
    def connect(self):    #Se define este método para establecer una conexión con la base de datos.
        try:              #El bloque "try" contiene:
            self.con = sqlite3.connect('dataBase.db')   #La conexión con la base de datos
            self.cur = self.con.cursor()                #Se crea este cursor para ejecutar consultas SQL.
        except sqlite3.Error as e:                      #Si hay un error durante la conexión, se detecta y muestra un mensaje de error
            print(f"Error connecting to database: {e}") #Este es el mensaje.

    def SQL(self, query, params=()):                    #Define el método "SQL", ademas de los parametros "query" (La consulta SQL) y "params"(Los parámetros de la consulta).
        try:                                            #Este bloque contiene.
            self.cur.execute(query, params)             #Intenta ejecutar la consulta "SQL" usando el cursor "self.cur" antes creado.
            if query.startswith('SELECT'):              #Si la consulta es un "Select" entonces:
                columns = [column[0] for column in self.cur.description]             #Obtiene las columnas de la tabla solicitada.
                result = [dict(zip(columns, row)) for row in self.cur.fetchall()]    #Cada fila de "fetchall()" se convierte en un diccionario.
                return result                                                        #Muestra el resultado.
            self.con.commit()                              #Si la consulta no es tipo "Select" se ejecuta "commit()"
        except sqlite3.Error as e:                         #Si ocurre un error al ejecutar la consulta, se muestra un mensaje de error.   
            print(f"Error executing query: {e}")           #Este es el mensaje.

    def close(self):                                       #Este método cierra la conexión la base de datos.
        try:                                              
            self.con.close()                                
        except sqlite3.Error as e:                         #Intenta cerra la conexión con la base de datos, si se logra muestra un mensaje.
            print(f"Error closing the connection: {e}")    #Este es el mensaje.
