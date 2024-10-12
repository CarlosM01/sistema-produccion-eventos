from views.welcome import Welcome  # Importamos la vista
from views.common import Common
from controllers.user_controller import UserController
from controllers.attendee_controller import AttendeeController

class MainController:
    def __init__(self):
        self.welcome_view = Welcome()
        self.common_view = Common()
        self.user_controller = UserController()
        self.attendee_controller = AttendeeController()

    def start(self):
        while True:
            option = self.welcome_view.menu()
            if option == 1:
                self.user_controller.login()
            elif option == 2:
                self.attendee_controller.register()
            elif option == 3:
                self.common_view.alert("Saliendo del sistema...")
                exit()