from models.crud import CRUDModel

class RoleModel(CRUDModel):
    def __init__(self):
        super().__init__()
        self.table_name = 'roles'
        self.create_table()

    def create_table(self):
        self.db.connect()        
        self.db.SQL(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                role_id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_name TEXT NOT NULL UNIQUE
            )
        ''')
        self.db.close()

    def create_role(self, data) -> dict:
        result = self.get_by_attribute('role_name', data['role_name'])
        if result:
            return {'message': 'Este rol ya existe'}
        self.post(data)
        return {'message': 'Rol registrado exitosamente'}
