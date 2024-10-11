from views import Views  # Importamos la vista
from controllers.authController import AuthController
from controllers.userController import UserController

class MainController:
    def __init__(self):
        self.views = Views()
        self.authController = AuthController()
        self.userController = UserController()

    def start(self):
        option = self.views.welcome()  # Mostramos el menú
        if option == 1:
            self.authController.login()  # Redirige al controlador de autenticación
        elif option == 2:
            self.userController.register()  # Redirige al controlador de registro de usuarios
        elif option == 3:
            print("Saliendo del sistema...")