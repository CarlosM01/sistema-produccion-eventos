import time

from services.session import Session

from models.locations import LocationsModel
from models.shows import ShowsModel
from models.users import UserModel

from views.admin import AdminView


class AdminController:
    def __init__(self):
        self.session = Session()
        self.locations_model = LocationsModel()
        time.sleep(0.5)
        self.shows_model = ShowsModel()
        self.user_model = UserModel()

        self.admin_view = AdminView()


    def menu(self):
        self.locations = self.locations_model.get_all()
        self.location_ids = [l['location_id'] for l in self.locations] if self.locations else []

        self.shows_recap = self.shows_model.get_shows_recap()
        self.show_ids = [s['show_id'] for s in self.shows_recap] if self.shows_recap else []

        # Diccionario que mapea opciones del menú a métodos específicos.
        menu_actions = {
            1: lambda: self._handle_locations(),
            2: lambda: self._create_show(),
            3: lambda: self._display_shows(),
            4: lambda: self._update_show(),
            5: lambda: self._delete_show(),
            6: lambda: self._update_personal_info(),
            7: lambda: self._log_out(),
            8: lambda: self._exit_system(),
        }

        self.user_data = self.session.get_active_user()
        option = self.admin_view.menu(self.user_data['name'])
        menu_actions.get(option)()

        return {'log_out': option == 7}
    

    def _handle_locations(self):
        self.locations = self.locations_model.get_all()
        self.location_ids = [l['location_id'] for l in self.locations]
        option = self.admin_view.locations_menu()        
        if option == 1:
            self.admin_view.display(self.locations)
            self._handle_locations()

        elif option == 2:
            data = self.admin_view.create_location()
            self.locations_model.post(data)
            self._handle_locations()

        elif option == 3:
            self.admin_view.display(self.locations)
            update = self.admin_view.update_location(self.location_ids)
            self.locations_model.update(update['id'], update['data']) if update['success'] else None
            self._handle_locations()

        elif option == 4:
            self.admin_view.display(self.locations)
            delete = self.admin_view.delete_location(self.location_ids)
            if delete['success']:
                self.locations_model.delete(delete['id']) 
                shows = self.shows_model.get_by_location(delete['id'])
                show_ids = [s['show_id'] for s in shows] if shows else []
                for id in show_ids:
                    self.shows_model.delete(id)
            self._handle_locations()


    def _create_show(self):
        if self.location_ids:
            self.admin_view.display(self.locations)
            location = self.admin_view.select_location(self.location_ids)
            if location['success']:
                data = self.admin_view.create_show()
                data['location_id'] = location['id']
                self.shows_model.post(data)
        else:
            self.admin_view.alert('No hay sedes disponibles. Registre una primero.')


    def _display_shows(self):
        self.admin_view.display(self.shows_recap)
        show = self.admin_view.select_show(self.show_ids)
        
        if show['success']:
            show_details = self.shows_model.get_shows_detail(show['id'])
            self.admin_view.display(show_details)


    def _update_show(self):
        self.admin_view.display(self.shows_recap)
        update = self.admin_view.update_show(self.show_ids)
        if update['success']:
            id = update['id']
            data = update['data']

            location = self.admin_view.update_location_show(self.location_ids)
            if location['success']:
                data['location_id'] = location['id']

            self.shows_model.update(id, data) 
                    

    def _delete_show(self):
        self.admin_view.display(self.shows_recap)
        delete = self.admin_view.delete_show(self.show_ids)
        if delete['success']:
            self.shows_model.delete(delete['id'])


    def _update_personal_info(self):
        data = self.admin_view.update_user()

        id = self.user_data['user_id']
        password = self.user_data['password']

        new_pass = self.admin_view.update_password(password)
        if new_pass:
            data['password'] = new_pass

        self.user_model.update(id, data)
        user_data = self.user_model.get_by_attribute('user_id', id)
        self.session.start_session(user_data)


    def _log_out(self):
        self.admin_view.alert('Cerrando sesión')

    def _exit_system(self):
        self.admin_view.alert('Saliendo del sistema...')
        exit()


        