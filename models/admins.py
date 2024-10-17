from models.users import UserModel #Se importa la clase UserModel.

class AdminModel(UserModel): #Se crea la clase AdminModel que hereda sus atributos de la clase anterior.
    def __init__(self): #Define el modulo constructor de la clase AdminModel.
        super().__init__() #Llama al constructor de la clase UserModel.
        self.role_id = 2 #Establece un atributo role_id en 2 indica que esta clase representa un administrador.

    def get_admin_list(self): #Define un metodo para obtener una lista de administradores.
        self.db.connect() #Esto conecta a la base de datos.
        result = self.db.SQL(f"SELECT * FROM {self.table_name} WHERE role_id = {self.role_id}") 
        #Ejecuta una consulta SQL que selecciona todos los registros de la tabla cuyo role_id sea igual a role_id
        self.db.close() #Esto cierra la coneccion con la base de datos.
        return result #Devuelve el resultado de la consulta.
