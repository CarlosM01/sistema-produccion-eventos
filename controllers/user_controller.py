from models.users import UserModel
from views.welcome import Welcome
from views.root import Root
from views.admin import Admin
from views.attendee import Attendee
from views.common import Common

class UserController:
    def __init__(self):
        self.user_model = UserModel()
        self.welcome_view = Welcome()
        self.root_view = Root()
        self.admin_view = Admin()
        self.attendee_view = Attendee()
        self.common_view = Common()

    def login(self):
        data = self.welcome_view.login()
        result = self.user_model.login(data['email'], data['password'])
        self.common_view.alert(result['message'])
        if result['success']:
            role = self.user_model.get_role(data['email'])
            self.redirect_to_dashboard(role['role_id'])

    def redirect_to_dashboard(self, role_id):
        if role_id == 1:
            self.root_view.watch()
        elif role_id == 2:
            self.admin_view.watch()
        elif role_id == 3:
            self.attendee_view.watch()