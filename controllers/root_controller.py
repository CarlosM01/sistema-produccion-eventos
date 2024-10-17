from models.root import RootModel                            #Importa la clase "RootModel".
from models.admins import AdminModel                         #Importa la clase "AdminModel".

from views.root_view import RootView                         #Importa la clase "RootView".
from views.common import Common                              #Importa la clase "Common".


class RootController:                                        #Esta clase actúa como controlador para el rol root, coordinando las interacciones entre los modelos de root y administradores
    def __init__(self):                                      #Este constructor inicializa modelos y vistas.
        self.root_model = RootModel()                        #Crea una instancia que gestiona la lógica de datos específica para el root.
        self.admin_model = AdminModel()                      #Crea una instancia del modelo de administradores para gestionar los datos de los administradores.
        self.root_view = RootView()                          #Crea una instancia de la vista "RootView" para manejar la interfaz de usuario relacionada al usuario root
        self.common_view = Common()                          #Crea una instancia de la vista "Common" para funciones comunes
        self.admins = self.admin_model.get_admin_list()      #Invoca al método "get_admin_list" para obtener la lista de todos los administradores y se almacena en "self.admins". 


    def menu(self):                                          #El método "menu" que controla el flujo del menú para el root.
        while True:                                            
            option = self.root_view.menu()                   #Invoca "RootView" para mostrar el menu del root y recoge la opción seleccionada.
            if option == 1:                                  #Si es esta opcion, entonces:
                self.root_view.display_admins(self.admins)   #Se invoca "display_admins" de "RootView" para mostrar la lista de administradores.
            if option == 2:                                  #Si es esta opcion, entonces:
                return {'register':True, 'role_id':2}        #Retorna un diccionario con register:True y role_id:2, lo que indica que se debe registrar un nuevo admin.
            if option == 3:                                  
                pass                
            if option == 4:
                pass
            if option == 5:
                return
            if option == 6:
                exit()

        
