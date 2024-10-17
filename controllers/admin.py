import time

from services.session import Session

from models.locations import LocationsModel
from models.shows import ShowsModel

from views.admin import AdminView


class AdminController:
    def __init__(self):
        self.session = Session()
        self.locations_model = LocationsModel()
        time.sleep(1)
        self.shows_model = ShowsModel()

        self.admin_view = AdminView()


    def menu(self):
        self.locations = self.locations_model.get_all()
        # Diccionario que mapea opciones del menú a métodos específicos.
        menu_actions = {
            1: lambda: self._handle_locations(),
            2: lambda: self._create_show(),
            3: lambda: self._display_shows(),

            7: lambda: self._log_out(),
            8: lambda: self._exit_system(),
        }

        user_data = self.session.get_active_user()
        option = self.admin_view.menu(user_data['name'])
        menu_actions.get(option)()

        return {'log_out': option == 7}
    
    def _handle_locations(self):
        option = self.admin_view.locations_menu()        
        if option == 1:
            self.admin_view.display(self.locations)
        elif option == 2:
            data = self.admin_view.create_location()
            self.locations_model.post(data)


    def _create_show(self):
        available_ids = [l['location_id'] for l in self.locations]
        
        if available_ids:
            location_id = self.admin_view.select_location(available_ids)
            data = self.admin_view.create_show()
            data['location_id'] = location_id['id']
            self.shows_model.post(data)
        else:
            self.admin_view.alert('No hay sedes disponibles. Registre una primero.')

    def _display_shows(self):
        shows_recap = self.shows_model.get_shows_recap()
        self.admin_view.display(shows_recap)

        available_ids = [s['show_id'] for s in shows_recap]
        show = self.admin_view.select_show(available_ids)
        
        if show['success']:
            show_details = self.shows_model.get_shows_detail(show['id'])
            self.admin_view.display(show_details)
        


    def _log_out(self):
        self.admin_view.alert('Cerrando sesión')

    def _exit_system(self):
        self.admin_view.alert('Saliendo del sistema...')
        exit()