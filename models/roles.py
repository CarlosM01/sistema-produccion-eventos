from models.crud import CRUDModel #Importa la clase CRUDModel desde models.crud.

class RoleModel(CRUDModel): #Crea la clase RoleModel, que hereda de CRUDModel.
    def __init__(self): #Define el constructor de la clase.
        super().__init__() #Se llama al método constructor de la clase padre, para iniciar la conexión con la base de datos y las funcionalidades heredadas.
        self.table_name = 'roles' #Asigna el nombre de la tabla como 'roles'. Esto especifica que la operaciones CRUD de esta clase se realizaran en la tabla 'roles'.
        self.create_table() #Este método se encarga de crear la tabla de roles en caso de ser necesario.

    def create_table(self): #Define un método que crea la tabla de 'roles' si no existe.
        self.db.connect() #Establece una conexión con la base de datos
        self.db.SQL(f'''
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                role_id INTEGER PRIMARY KEY AUTOINCREMENT,
                role_name TEXT NOT NULL UNIQUE
            ) 
        ''') #Ejecuta una consulta SQL para crear la tabla 'roles' si no ha sido creada. teniendo las columnas 'roles_id' y 'role_name'.
        self.db.close() #Cierra la conexión a la base de datos

    def create_role(self, data) -> dict: # Define un método que recibe el diccionario 'data', y se encarga de crear un nuevo rol en la base de datos.
        result = self.get_by_attribute('role_name', data['role_name']) #Utiliza el método get_by_attribute para verificar si ya exite un rol con el nombre entregado
        if result:#Si encuentra un resultado, entonces muestra el mensaje:
            return {'message': 'Este rol ya existe'} #Muestra un mensaje indicando que el rol no se puede crear porque ya existe
        self.post(data) #Si el rol no existe, usa el método post heredado de CRUDModel para insertar el nuevo rol en la base de datos.
        return {'message': 'Rol registrado exitosamente'} #Devuelve un mensaje indicando que el rol ha sido creado exitosamente.
