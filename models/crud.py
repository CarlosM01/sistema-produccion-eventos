from db import DataBase

class CRUDModel:
    def __init__(self):
        self.db = DataBase()

    def post(self, data:dict):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        self.db.connect()
        self.db.SQL(query, tuple(data.values()))
        self.db.close()

    def get_by_attribute(self, column:str, value:str):
        self.db.connect()
        query = f"SELECT * FROM {self.table_name} WHERE {column} = ?"
        result = self.db.SQL(query, (value,))
        self.db.close()
        return result[0] if result else None

    def get_all(self):
        self.db.connect()
        result = self.db.SQL(f"SELECT * FROM {self.table_name}")
        self.db.close()
        return result

    def update(self, id:int, data: dict) -> dict:
        self.db.connect()
        fields = ', '.join([f"{key} = ?" for key in data.keys()])
        id_field = self.table_name.rstrip('s')
        query = f'UPDATE {self.table_name} SET {fields} WHERE {id_field}_id = ?'
        self.db.SQL(query, (*data.values(), id))
        self.db.close()
        return {'message': 'Registro actualizado exitosamente'}

    def delete(self, item_id:int):
        self.db.connect()
        id_field = self.table_name.rstrip('s')
        self.db.SQL(f"DELETE FROM {self.table_name} WHERE {id_field}_id = ?", (item_id,))
        self.db.close()