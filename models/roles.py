from db import DataBase

class Role:
    def __init__(self):
        self.db = DataBase()
        self.create_table()

    def create_table(self):
        self.db.connect()        
        self.db.SQL('''
            CREATE TABLE IF NOT EXISTS roles (
                role_id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_name TEXT NOT NULL UNIQUE
            )
        ''')
        self.db.close()

    def get(self):
        self.db.connect()
        result = self.db.SQL('SELECT * FROM roles')
        self.db.close()
        if result:
            return result

    def get_by_name(self, name):
        self.db.connect()
        result = self.db.SQL('SELECT * FROM roles WHERE role_name = ?', (name,))
        self.db.close()
        if result:
            return result[0]

    def post(self, role_name: str) -> dict:
        self.db.connect()
        result = self.db.SQL('SELECT * FROM roles WHERE role_name = ?', (role_name,))
        if result:
            return {'message': 'Este rol ya existe'}
        self.db.SQL('''
            INSERT INTO roles (role_name)
            VALUES (?)
        ''', (role_name,))
        self.db.close()
        return {'message': 'Rol registrado exitosamente'}

    def patch(self, role_id, role_name=None):
        self.db.connect()

        # actualiza el nombre del rol si es necesario
        if role_name:
            self.db.SQL('''
                UPDATE roles SET role_name = ? WHERE role_id = ?
            ''', (role_name, role_id))

        self.db.close()

    def delete(self, role_id):
        self.db.connect()
        self.db.SQL('DELETE FROM roles WHERE role_id = ?', (role_id,))
        self.db.close()