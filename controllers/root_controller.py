from models.root import RootModel
from models.admins import AdminModel

from views.root_view import RootView
from views.common import Common


class RootController:
    def __init__(self):
        self.root_model = RootModel()
        self.admin_model = AdminModel()
        self.root_view = RootView()
        self.common_view = Common()

        self.admins = self.admin_model.get_admin_list()


    def menu(self):
        while True:
            option = self.root_view.menu()
            if option == 1:
                self.root_view.display_admins(self.admins)
            if option == 2:
                return {'register':True, 'role_id':2}
            if option == 3:
                pass
            if option == 4:
                pass
            if option == 5:
                return
            if option == 6:
                exit()

        