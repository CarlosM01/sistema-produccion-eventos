from models.users import UserModel
from models.root import RootModel
from models.admins import AdminModel
from models.attendees import AttendeeModel

from views.welcome import Welcome
from views.root_view import RootView
from views.admin import Admin
from views.attendee import Attendee
from views.common import Common

from controllers.root_controller import RootController


class UserController:
    def __init__(self):
        self.user_model = UserModel()
        self.root_model = RootModel()
        self.admin_model = AdminModel()
        self.attendee_model = AttendeeModel()

        self.welcome_view = Welcome()
        self.root_view = RootView()
        self.admin_view = Admin()
        self.attendee_view = Attendee()
        self.common_view = Common()

        self.root_controller = RootController()


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

    