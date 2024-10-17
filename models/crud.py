from db import DataBase #Se importa la clase DataBase.

class CRUDModel: #Se crea la clase CRUDModel.
    def __init__(self): #Define el método constructor, creando una instancia de la clase.
        self.db = DataBase() #Crea la instancia db dentro de la clase.

    def post(self, data): #Define el método post para insertar un nuevo registro en la base de datos, data es un diccionario con columnas y valores correspondientes.
        columns = ', '.join(data.keys()) #Crea una cadena con los nombres de las columnas separadas por comas, provenientes del diccionario data.
        placeholders = ', '.join(['?'] * len(data)) #Crea signos de interrogacion, separados por comas, servirán como marcadores de posición para los valores en SQL, provenientes de data. 
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})" #Crea una consulta SQL para agregar datos a la tabla sel.table_name, utilizando las columnas y marcadores ya creados.
        self.db.connect() #Establece una conexión con la base de datos.
        self.db.SQL(query, tuple(data.values())) #Ejecuta la consulta SQL, para ser agregadas al diccionario data.
        self.db.close() #Cierra la conexión con la base de datos

    def get_by_attribute(self, column, value): #Define el método get_by_attribute, que se usa para recuperar un registo en función de una columna y un valor específicos.
        self.db.connect() #Establece una conexión con la base de datos.
        query = f"SELECT * FROM {self.table_name} WHERE {column} = ?" #Crea una consulta SQL que selecciona todos los registros de la tabla donde el valor de la columna es igual al parametro value.
        result = self.db.SQL(query, (value,)) #Ejecuta la consulta SQL, pasando el valor como parámetro.
        self.db.close() #Cierra la conexión con la base de datos.
        return result[0] if result else None #Devuelve el primer resultado de la consulta si se encontraron registros, o None si no se encontró ningún resultado.

    def get_all(self): #Define un método que recupera todos los registros de la tabla correspondiente.
        self.db.connect() #Conecta con la base de datos.
        result = self.db.SQL(f"SELECT * FROM {self.table_name}") #Ejecuta una consulta SQL que selecciona todos los registros de la tabla.
        self.db.close() #Cierra la conexión.
        return result #Retorna los resultados de la consulta.
"""" """"
    def update(self, record_id, data: dict) -> dict: #Define el método update, que actualiza un registro en la base de datos, tomando la id de la tabla y el diccionario data que contiene los valores.
        self.db.connect() #Conecta con la base de datos.
        fields = ', '.join([f"{key} = ?" for key in data.keys()]) #Crea una cadena que representa las asignaciones de columnas para la consulta SQL de actualizacion
        sql = f'UPDATE {self.table_name} SET {fields} WHERE {self.table_name}_id = ?' #Crea una consulta SQL de actualización, se debe especificar que campo actualizar y en que registro, en record_id.
        self.db.SQL(sql, (*data.values(), record_id)) #Ejecuta la consulta SQL, pasando los valores a actualizar y el ID del registro.
        self.db.close() #Cierra la conexión a la base de datos.
        return {'message': 'Registro actualizado exitosamente'} #Retorna un mensaje indicando que la actualizacion fue exitosa.

    def delete(self, item_id): #Define un método para eliminar un registro de la base de datos. Toma el parámetro item_id, que es el ID del registro.
        self.db.connect() #Establece la conexión con la base de datos.
        self.db.SQL(f"DELETE FROM {self.table_name} WHERE id = ?", (item_id,)) #Ejecuta una consulta SQL que elimina el registro cuyo ID es igual a item_id
        self.db.close() #Cierra la conexión a la base de datos.
