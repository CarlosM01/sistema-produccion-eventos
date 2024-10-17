from models.users import UserModel
from models.root import RootModel
from models.admins import AdminModel

from views.root import RootView


class RootController:
    def __init__(self): 
        self.user_model = UserModel()
        self.root_model = RootModel()
        self.admin_model = AdminModel()
        self.root_view = RootView()


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
            update = self.root_view.update_admin(availables_id)    
            self.user_model.update(update['id'], update['data']) if update['success'] else None
        if option == 4:
            delete = self.root_view.delete_admin(availables_id)
            self.user_model.delete(delete['id']) if delete['success'] else None
        if option == 5:
            self.root_view.alert('Cerrando sesión')
            res['log_out'] = True
        if option == 6:
            self.root_view.alert('Saliendo del sistema...')
            exit()
        return res

        