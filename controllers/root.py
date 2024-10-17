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
        available_ids = [user['user_id'] for user in admins] if admins else []

        # Diccionario que mapea opciones del menú a métodos específicos.
        menu_actions = {
            1: lambda: self.root_view.display(admins),
            2: lambda: self._handle_register(),
            3: lambda: self._update_admin(available_ids),
            4: lambda: self._delete_admin(available_ids),
            5: lambda: self._log_out(),
            6: lambda: self._exit_system()
        }

        option = self.root_view.menu()
        menu_actions.get(option)()

        return {'register': option == 2, 'log_out': option == 5}

    def _handle_register(self):
        self.root_view.alert('Registrar nuevo usuario')

    def _update_admin(self, available_ids):
        update = self.root_view.update_admin(available_ids)
        if update['success']:
            self.user_model.update(update['id'], update['data'])
            self.root_view.alert('Administrador actualizado exitosamente')

    def _delete_admin(self, available_ids):
        delete = self.root_view.delete_admin(available_ids)
        if delete['success']:
            self.user_model.delete(delete['id'])
            self.root_view.alert('Administrador eliminado exitosamente')

    def _log_out(self):
        self.root_view.alert('Cerrando sesión')

    def _exit_system(self):
        self.root_view.alert('Saliendo del sistema...')
        exit()



        