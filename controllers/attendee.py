from services.session import Session

from models.locations import LocationsModel
from models.shows import ShowsModel
from models.reservations import ReservationsModel
from models.users import UserModel

from views.attendee import AttendeeView


class AttendeeController:
    def __init__(self):
        self.session = Session()
        self.locations_model = LocationsModel()
        self.shows_model = ShowsModel()
        self.reservations_model = ReservationsModel()
        self.user_model = UserModel()
        self.attendee_view = AttendeeView()

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
    
    @property
    def reservations(self):
        recap = self.reservations_model.reservations_recap(self.user_data['user_id'])
        return recap, [res['reservation_id'] for res in recap]

    def menu(self):
        self.logout = False
        self.user_data = self.session.get_active_user()
        option = self.attendee_view.menu(self.user_data['name'])

        # Diccionario de acciones del menú.
        menu_actions = {
            1: self._new_reservation,
            2: self._display_reservations,
            3: self._delete_reservation,
            4: self._update_personal_info,
            5: self._log_out,
            6: self._exit_system,
        }

        action = menu_actions.get(option)
        if action:
            action()

        return {'log_out': self.logout}


    def _new_reservation(self):
        shows_recap, show_ids = self.shows
        self.attendee_view.display(shows_recap)

        selected_show = self.attendee_view.select_show(show_ids)
        if selected_show['success']:
            self._process_show(selected_show['id'])
    
    def _process_show(self, show_id):
        details = self.shows_model.get_show_details(show_id)
        self.attendee_view.display(details)
        if self.attendee_view.buy_ticket(details):
            self._create_reservation(details) 

    #Este metodo necesita ser optimizado
    def _create_reservation(self, details):
        self.shows_model.update_reservations(1, details['show_id']) #Esto deberia estar centralizado en ReservationsModels
        data = {
            'user_id':self.user_data['user_id'], 
            'show_id':details['show_id']
            }
        ticket = self.reservations_model.create_reservation(data)
        self.attendee_view.display_ticket(ticket)

             
    def _display_reservations(self):
        reservations_recap, reservations_ids = self.reservations

        self.attendee_view.display(reservations_recap)
        option = self.attendee_view.select_show(reservations_ids)
        if option['success']:
            ticket = self.reservations_model.get_ticket_details(option['id'])
            self.attendee_view.display(ticket)

    
    def _delete_reservation(self):
        reservations_recap, reservations_ids = self.reservations

        self.attendee_view.display(reservations_recap)
        option = self.attendee_view.select_show(reservations_ids)
        if option['success']:
            if self.attendee_view.delete_reservation():
                res = self.reservations_model.get_by_attribute('reservation_id', option['id'])
                self.reservations_model.delete(option['id'])
                self.shows_model.update_reservations(-1, res['show_id'])
        

    #Logica duplicada con el rol de administrador, considerar centralizar esta caracteristica
    def _update_personal_info(self):
        user_data = self.user_data
        updated_info = self.attendee_view.update_user()

        new_pass = self.attendee_view.update_password(user_data['password'])
        if new_pass:
            updated_info['password'] = new_pass

        self.user_model.update(user_data['user_id'], updated_info)
        self.session.start_session(self.user_model.get_by_attribute('user_id', user_data['user_id']))

    def _log_out(self):
        self.logout = self.attendee_view.log_out()

    def _exit_system(self):
        exit() if self.attendee_view.exit_system() else None
