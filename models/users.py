from models.crud import CRUDModel #Se importa la clase CRUDModel.

class UserModel(CRUDModel): #Se crea la clase "UserModel" y hereda los atributos de "CRUDModel".
    def __init__(self): #Define el constructor de la clase "UserModel", se ejecuta para crear una instancia dentro de la clase.
        super().__init__() #Se invoca al constructor de la clase padre "CRUDModel" para inicializar las propiedades heredadas.
        self.table_name = 'users' #Define que la tabla "users" esta asosiciada a esta clase.
        self.create_table() #Invoca al método "create_table" para que la tabla usuarios sea creada en caso de que no exista. 

    def create_table(self): #Crea la tabla users si no existe.
        self.db.connect() #Se conecta con la base de datos
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
        self.db.close() #Cierra la conexion con la base de datos.
        
    def get_role(self, email) -> dict: #Método que obtiene el role_id de un usuario por su email.
        self.db.connect() #Se conecta con la base de datos.
        result = self.db.SQL('SELECT role_id FROM users WHERE email = ?', (email,)) #Ejecuta una consulta SQL para buscar el dato solicitado.
        self.db.close() #Cierra la conexion con la base de datos.
        if result: #Si encuentra un resultado, lo devuelve.
            return result[0] #Se muestra el resultado.

    def register(self, data: dict) -> dict: #Método para registrar usuarios en la base de datos a traves de sus correos.
        result = self.get_by_attribute('email', data['email']) #Verifica si el usuario existe en la base de datos.
        if (result): #Si encuentra el resultado, lo devuelve.
            return {'message': 'Este email ya ha sido registrado previamente'} 
        data['role_id'] = self.role_id #Asigna un "role_id" al usuario creado, dependiendo del rango que tenga en el sistema.
        self.post(data) #Invoca al método "post" para insertar al nuevo usuario en la base de datos.
        return {'message': 'Usuario registrado exitosamente'}
    
    def login(self, email, password) -> dict: #Método para iniciar sesión de un usuario.
        user = self.get_by_attribute('email', email) #Busca un usuario con el correo proporcionado.
        if user: #Si encuetra el resultado, lo devuelve:
            if user['password'] == password:
                return {'success': True, 'message': 'Iniciar sesión...'}
            else: #Si la contraseña es incorrecta entonces:
                return {'success': False, 'message': 'Contraseña incorrecta'}
        else: #Si no encuentra nada:
            return {'success': False, 'message': 'Este email no se encuentra registrado'}
