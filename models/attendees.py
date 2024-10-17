from models.users import UserModel #Importa la clase UserModel desde el archivo modeld.users.

class AttendeeModel(UserModel): #Se crea la clase AttendeeModel que heredara los atributos de las UserModel.
    def __init__(self): #Define el metodo constructor de la clase, creando una instancia dentro de la misma.
        super().__init__() #Se invoca la clase UserModel para que herede sus atributos.
        self.role_id = 3 #Se asigna el valor de 3 a la clase creada
        
    def view_content(self): #Permite acesso el acceso a la informacion, de acuerdo al rango en el sistema.
        pass 
