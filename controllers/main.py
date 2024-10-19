from models.users import UserModel
from models.root import RootModel
from models.admins import AdminModel
from models.attendees import AttendeeModel
from services.session import Session

from views.welcome import WelcomeView 
from views.common import CommonView

from controllers.root import RootController
from controllers.admin import AdminController
from controllers.attendee import AttendeeController


class MainController:
    def __init__(self):
        # Modelos
        self.session = Session()
        self.user_model = UserModel()
        self.root_model = RootModel()
        self.admin_model = AdminModel()
        self.attendee_model = AttendeeModel()

        # Vistas
        self.welcome_view = WelcomeView()
        self.common_view = CommonView()

        # Controladores
        self.root_controller = RootController()
        self.admin_controller = AdminController()
        self.attendee_controller = AttendeeController()


    def redirect_to_dashboard(self):
        while True:
            active_user = self.session.get_active_user()
            if not active_user:
                return self.main_menu()  # Salida temprana si no hay sesión activa

            role_id = active_user['role_id']
            dashboard_actions = {
                1: self._handle_root_dashboard,
                2: self._handle_admin_dashboard,
                3: lambda: self.common_view.alert('Attendee Dashboard'),
            }
            dashboard_actions.get(role_id, self._invalid_role)()  # Ejecuta la acción según el rol


    def main_menu(self):
        while True:
            option = self.welcome_view.menu()
            if option == 1:
                self.login()
            elif option == 2:
                self.register()
            elif option == 3:
                exit() if self.common_view.exit_system() else None
            

    def register(self):
        data = self.common_view.register()
        role_id = self._determine_role()
        model = self._get_role_model(role_id)

        if model:
            result = model.register(data)
            self.common_view.alert(result['message'])


    def login(self):
        data = self.welcome_view.login()
        result = self.user_model.login(data['email'], data['password'])
        self.common_view.alert(result['message'])

        if result['success']:
            user_data = self.user_model.get_by_attribute('email', data['email'])
            self.session.start_session(user_data)
        
        self.redirect_to_dashboard()


    def _handle_root_dashboard(self):
        res = self.root_controller.menu()
        if res.get('register'):
            self.register()
        if res.get('log_out'):
            self.session.end_session()


    def _handle_admin_dashboard(self):
        res = self.admin_controller.menu()
        if res.get('log_out'):
            self.session.end_session()

    
    def _handle_attendee_dashboard(self):
        res = self.attendee_controller.menu()
        if res.get('log_out'):
            self.session.end_session()


    def _determine_role(self):
        active_user = self.session.get_active_user()
        return 2 if active_user and active_user['role_id'] == 1 else 3


    def _get_role_model(self, role_id):
        role_models = {
            1: self.root_model,
            2: self.admin_model,
            3: self.attendee_model
        }
        return role_models.get(role_id)


    def _invalid_role(self):
        self.common_view.alert("Rol no reconocido.")