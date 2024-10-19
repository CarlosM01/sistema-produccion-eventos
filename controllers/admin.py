from services.session import Session

from models.locations import LocationsModel
from models.shows import ShowsModel
from models.users import UserModel

from views.admin import AdminView


class AdminController:
    def __init__(self):
        self.session = Session()
        self.locations_model = LocationsModel()
        self.shows_model = ShowsModel()
        self.user_model = UserModel()
        self.admin_view = AdminView()

    @property
    def locations(self):
        """Obtiene las sedes y sus IDs."""
        locations = self.locations_model.get_all()
        return locations, [loc['location_id'] for loc in locations]

    @property
    def shows(self):
        """Obtiene los shows y sus IDs."""
        recap = self.shows_model.get_shows_recap()
        return recap, [show['show_id'] for show in recap]

    def menu(self):
        self.logout = False
        self.user_data = self.session.get_active_user()
        option = self.admin_view.menu(self.user_data['name'])

        # Diccionario de acciones del menú.
        menu_actions = {
            1: self._handle_locations,
            2: self._create_show,
            3: self._display_shows,
            4: self._update_show,
            5: self._delete_show,
            6: self._update_personal_info,
            7: self._log_out,
            8: self._exit_system,
        }

        action = menu_actions.get(option)
        if action:
            action()

        return {'log_out': self.logout}


    def _handle_locations(self):
        while True:
            locations, location_ids = self.locations
            option = self.admin_view.locations_menu()
            if option == 1:
                self.admin_view.display(locations)
            elif option == 2:
                self._create_location()
            elif option == 3:
                self._update_location(location_ids)
            elif option == 4:
                self._delete_location(location_ids)
            else:
                break  # Salir del submenú

    def _create_location(self):
        data = self.admin_view.create_location()
        self.locations_model.post(data)

    def _update_location(self, location_ids):
        update = self.admin_view.update_location(location_ids)
        if update['success']:
            self.locations_model.update(update['id'], update['data'])

    def _delete_location(self, location_ids):
        delete = self.admin_view.delete_location(location_ids)
        if delete['success']:
            self.locations_model.delete(delete['id'])
            self._delete_shows_by_location(delete['id'])

    def _delete_shows_by_location(self, location_id):
        shows = self.shows_model.get_by_location(location_id)
        if shows:
            for show in shows:
                self.shows_model.delete(show['show_id'])

    def _create_show(self):
        locations, location_ids = self.locations
        if not location_ids:
            self.admin_view.alert('No hay sedes disponibles. Registre una primero.')
            return

        self.admin_view.display(locations)
        location = self.admin_view.select_location(location_ids)
        if location['success']:
            data = self.admin_view.create_show()
            self.shows_model.create_show(data, location['id'])

    def _display_shows(self):
        shows_recap, show_ids = self.shows
        self.admin_view.display(shows_recap)
        show = self.admin_view.select_show(show_ids)
        if show['success']:
            details = self.shows_model.get_show_details(show['id'])
            self.admin_view.display(details)

    def _update_show(self):
        shows_recap, show_ids = self.shows
        self.admin_view.display(shows_recap)

        update = self.admin_view.update_show(show_ids)
        if update['success']:
            self._apply_show_update(update)

    def _apply_show_update(self, update):
        location_ids = self.locations[1]
        data = update['data']

        location = self.admin_view.update_location_show(location_ids)
        if location['success']:
            data['location_id'] = location['id']

        self.shows_model.update(update['id'], data)

    def _delete_show(self):
        shows_recap, show_ids = self.shows
        self.admin_view.display(shows_recap)

        delete = self.admin_view.delete_show(show_ids)
        if delete['success']:
            self.shows_model.delete(delete['id'])

    def _update_personal_info(self):
        user_data = self.user_data
        updated_info = self.admin_view.update_user()

        new_pass = self.admin_view.update_password(user_data['password'])
        if new_pass:
            updated_info['password'] = new_pass

        self.user_model.update(user_data['user_id'], updated_info)
        self.session.start_session(self.user_model.get_by_attribute('user_id', user_data['user_id']))

    def _log_out(self):
        self.logout = self.admin_view.log_out()

    def _exit_system(self):
        exit() if self.admin_view.exit_system() else None
