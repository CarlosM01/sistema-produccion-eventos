from models.users import UserModel            #Importa la clase UserModel.
from models.root import RootModel             #Importa la clase RootModel.
from models.admins import AdminModel          #Importa la clase AdimModel.
from models.attendees import AttendeeModel    #Importa la clase AttendeeModel.

from views.welcome import Welcome             #Importa la clase Welcome.
from views.common import Common               #Importa la clase Common.

from controllers.user_controller import UserController             #Importa el controlador UserController.
from controllers.attendee_controller import AttendeeController     #Importa el controlador AttendeeController.
from controllers.root_controller import RootController             #Importa el controlador RootController.


class MainController:                           #Define la clase principal, cordina todas las interacciones del sistema, osea un controlador con el patrón MVC.
    def __init__(self):                         #El constructor de la clase, inicializa los modelos, vistas y controladores.
        self.user_model = UserModel()           #Se crea la instancia del modelo "UserModel".
        self.root_model = RootModel()           #Se crea la instancia del modelo "RootModel".
        self.admin_model = AdminModel()         #Se crea la instancia del modelo "AdminModel".
        self.attendee_model = AttendeeModel()   #Se crea la instancia del modelo "AttendeeModel".

        self.welcome_view = Welcome()                       #Se crea la instancia de las vistas "Welcome".
        self.common_view = Common()                         #Se crea la instancia de las vistas "Common".
        self.user_controller = UserController()             #Se crea la instancia de las vistas "UserController".
        self.root_controller = RootController()             #Se crea la instancia de las vistas "RootController".
        self.attendee_controller = AttendeeController()     #Se crea la instancia de las vistas "AttendeeController".


    def start(self):                            #Se define el método "Start" que inicia el flujo principal del programa.
        while True:                             #Se ejecuta indefinidamente hasta que el usurio decida salir.
            option = self.welcome_view.menu()   #Invoca a la vista "Welcome" para mostrar el menú principal y obtener la opción seleccionada.
            if option == 1:                     #Primera opcion.
                result = self.login()           #Invoca al método "login" para iniciar sesión. 
                self.redirect_to_dashboard(result['role_id']) if result['success'] else None #Si el inicio es exitoso, redirige al usuario al tablero acorde a su rol.
            elif option == 2:                   #Segunda opcion.
                self.register(3)                #Invoca al método "register" y "role_id" para que el usuario se registre.
            elif option == 3:                   #Tercera opcion.
                self.common_view.alert("Saliendo del sistema...")   #Muestra un mensaje de salida y temina el programa.
                exit() #Finaliza el programa.


    def register(self, role_id):                            #Este método registra usuarios en el sistema.
        data = self.common_view.register()                  #Obtiene los datos de registro mediante "Common".

        role_models = {                                     #Crea un diccionario que asocia cada "role_id".
            1: self.root_model,                             #Se agrega el rol "root".
            2: self.admin_model,                            #Se agrega el rol "admin".
            3: self.attendee_model                          #Se agrega el rol "attendee".
        }
        model = role_models.get(role_id)                    #Obtiene el modelo según el "role_id" como argumento.
        if model:                                           #Si el modelo existe: 
            result = model.register(data)                   #Registra los datos en la base de datos usando el modelo que corresponda.
            self.common_view.alert(result['message'])       #Muestra un mensaje de error o éxito.
            

    def login(self):                                                            #Este método maneja el inicio de sesión de los usuarios.
        data = self.welcome_view.login()                                        #Obtiene el email y contraseña de la vista "Welcome"
        result = self.user_model.login(data['email'], data['password'])         #Invoca el método "login" para autenticar al usuario.
        self.common_view.alert(result['message'])                               #Muestra un mensaje de error o exito.
        if result['success']:                                                   #Si el inicio de sesión es exitoso, obtiene el rol y lo devuelve con el estado de exito.
            role = self.user_model.get_role(data['email'])
            return {'success': True, 'role_id': role['role_id']}
    

    def redirect_to_dashboard(self, role_id):                                   #Este método redirige al usuario al menú correspondiente a su rol.
        if role_id == 1:                                                        #Si el rol es 1: (root):
            result = self.root_controller.menu()                                #Llama al manú del "RootController".
            self.register(result['role_id']) if result['register'] else None
        if role_id == 2:                                                        #Si el rol es 2 (admin):
            self.admin_view.watch()                                             #Redirige a la vista de administración.
        if role_id == 3:                                                        #Si el rol es 3 (asistente):
            self.attendee_view.watch()                                          #Redirige a la vista asistente.
