from models.crud import CRUDModel

class UserModel(CRUDModel):
    def __init__(self):
        super().__init__()
        self.table_name = 'users'
        self.create_table()

    def create_table(self):
        self.db.connect()        
        self.db.SQL(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                phone INTEGER NOT NULL,
                password TEXT NOT NULL,
                role_id INTEGER,
                FOREIGN KEY (role_id) REFERENCES roles(role_id)    
            )
        ''')
        self.db.close()
        
    def get_role(self, email) -> dict:
        self.db.connect()
        result = self.db.SQL('SELECT role_id FROM users WHERE email = ?', (email,))
        self.db.close()
        if result:
            return result[0]

    def register(self, data: dict) -> dict:
        result = self.get_by_attribute('email', data['email'])
        if (result):
            return {'message': 'Este email ya ha sido registrado previamente'}
        data['role_id'] = self.role_id
        self.post(data)
        return {'message': 'Usuario registrado exitosamente'}
    
    def login(self, email, password) -> dict:
        user = self.get_by_attribute('email', email)
        if user:
            if user['password'] == password:
                return {'success': True, 'message': 'Iniciar sesión...'}
            else:
                return {'success': False, 'message': 'Contraseña incorrecta'}
        else:
            return {'success': False, 'message': 'Este email no se encuentra registrado'}