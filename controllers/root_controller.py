from models.users import UserModel
from models.root import RootModel
from models.admins import AdminModel

from views.root import RootView
from views.common import CommonView


class RootController:
    def __init__(self): 
        self.user_model = UserModel()
        self.root_model = RootModel()
        self.admin_model = AdminModel()
        self.root_view = RootView()
        self.common_view = CommonView()


    def menu(self):
        admins = self.admin_model.get_admin_list()
        if admins:
            availables_id = []
            for user in admins:
                    availables_id.append(user['user_id'])
        res = {'register':False, 'log_out':False}

        option = self.root_view.menu()
        if option == 1:
            self.root_view.display_admins(admins)
        if option == 2:
            res['register'] = True
        if option == 3:
            data = self.common_view.update_user(availables_id)
            self.user_model.update(data[0],data[1])
        if option == 4:
            pass
        if option == 5:
            res['log_out'] = True
        if option == 6:
            exit()
        return res

        