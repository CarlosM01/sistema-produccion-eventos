from models.users import UserModel
from models.root import RootModel
from models.admins import AdminModel
from models.attendees import AttendeeModel
from services.session import SessionModel

from views.welcome import Welcome 
from views.common import CommonView

from controllers.user_controller import UserController
from controllers.attendee_controller import AttendeeController
from controllers.root_controller import RootController

class MainController:
    def __init__(self):
        self.session_model = SessionModel()
        self.user_model = UserModel()
        self.root_model = RootModel()
        self.admin_model = AdminModel()
        self.attendee_model = AttendeeModel()
        

        self.welcome_view = Welcome()
        self.common_view = CommonView()
        self.user_controller = UserController()
        self.root_controller = RootController()
        self.attendee_controller = AttendeeController()


    def redirect_to_dashboard(self):
        while True:
            active_user = self.session_model.get_active_user()
            if active_user: 
                if active_user['role_id'] == 1:
                    res = self.root_controller.menu()
                    self.register() if res['register'] else None
                    self.session_model.end_session() if res['log_out'] else None
                if active_user['role_id'] == 2:
                    self.common_view.alert('Admin Dashboard')
                if active_user['role_id'] == 3:
                    self.common_view.alert('Attendee Dashboard')
            else: self.main_menu()


    def main_menu(self):
        option = self.welcome_view.menu()
        if option == 1:
            self.login()
        if option == 2:
            self.register()
        if option == 3:
            self.common_view.alert("Saliendo del sistema...")
            exit()


    def register(self):
        data = self.common_view.register()
        active_user = self.session_model.get_active_user()
        if active_user:
            role_id = active_user['role_id']
            use_model = 2 if role_id == 1 else None
                
        else: use_model = 3

        #Si se agregan mas roles en el futuro deberan mencionarse en este diccionario
        role_models = {
            1: self.root_model,
            2: self.admin_model,
            3: self.attendee_model
        }
        model = role_models.get(use_model)
        if model:
            result = model.register(data)
            self.common_view.alert(result['message'])
            

    def login(self):
        data = self.welcome_view.login()
        result = self.user_model.login(data['email'], data['password'])
        self.common_view.alert(result['message'])
        if result['success']:
            user_data = self.user_model.get_by_attribute('email', data['email'])
            self.session_model.start_session(user_data)
            self.redirect_to_dashboard()