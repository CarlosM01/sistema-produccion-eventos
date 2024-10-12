from models.attendees import AttendeeModel
from views.attendee import Attendee
from views.common import Common

class AttendeeController:
    def __init__(self):
        self.attendee_model = AttendeeModel()
        self.attendee_view = Attendee()
        self.common_view = Common()

    def register(self):
        data = self.common_view.register()
        result = self.attendee_model.register(data)        
        self.common_view.alert(result['message'])