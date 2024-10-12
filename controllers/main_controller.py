from models.users import UserModel
from models.root import RootModel
from models.admins import AdminModel
from models.attendees import AttendeeModel

from views.welcome import Welcome 
from views.common import Common

from controllers.user_controller import UserController
from controllers.attendee_controller import AttendeeController
from controllers.root_controller import RootController


class MainController:
    def __init__(self):
        self.user_model = UserModel()
        self.root_model = RootModel()
        self.admin_model = AdminModel()
        self.attendee_model = AttendeeModel()

        self.welcome_view = Welcome()
        self.common_view = Common()
        self.user_controller = UserController()
        self.root_controller = RootController()
        self.attendee_controller = AttendeeController()


    def start(self):
        while True:
            option = self.welcome_view.menu()
            if option == 1:
                result = self.login()
                self.redirect_to_dashboard(result['role_id']) if result['success'] else None
            elif option == 2:
                self.register(3)
            elif option == 3:
                self.common_view.alert("Saliendo del sistema...")
                exit()


    def register(self, role_id):
        data = self.common_view.register()

        role_models = {
            1: self.root_model,
            2: self.admin_model,
            3: self.attendee_model
        }
        model = role_models.get(role_id)
        if model:
            result = model.register(data)
            self.common_view.alert(result['message'])
            

    def login(self):
        data = self.welcome_view.login()
        result = self.user_model.login(data['email'], data['password'])
        self.common_view.alert(result['message'])
        if result['success']:
            role = self.user_model.get_role(data['email'])
            return {'success': True, 'role_id': role['role_id']}
    

    def redirect_to_dashboard(self, role_id):
        if role_id == 1:
            result = self.root_controller.menu()
            self.register(result['role_id']) if result['register'] else None
        if role_id == 2:
            self.admin_view.watch()
        if role_id == 3:
            self.attendee_view.watch()