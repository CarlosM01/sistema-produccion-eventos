from views.welcome import Welcome  # Importamos la vista
from views.alert import alert
from controllers.user_controller import UserController

class MainController:
    def __init__(self):
        self.welcome_view = Welcome()
        self.user_controller = UserController()

    def start(self):
        while True:
            option = self.welcome_view.menu()
            if option == 1:
                self.user_controller.login()
            elif option == 2:
                self.user_controller.register()
            elif option == 3:
                alert("Saliendo del sistema...")
                exit()