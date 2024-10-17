from models.users import UserModel #Importa la clase UserModel desde el módulo models.users.

class RootModel(UserModel): #Crea la clase RootModel que hereda todos las propiedades de UserModel.
    def __init__(self): #Define el constructor de la clase para crear una instancia.
        super().__init__() #Llama al constructor de la clase padre, para iniciar las propiedades heredadas.
        self.role_id = 1 #Se le asigna el valor de 1 a la ID de esta clase.

    def create_admin(self): #Esto permite a la clase RootModel el crear administradores.
        pass
