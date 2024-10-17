from models.attendees import AttendeeModel
from views.attendee import AttendeeView
from views.common import CommonView

class AttendeeController:
    def __init__(self):
        self.attendee_model = AttendeeModel()
        self.attendee_view = AttendeeView()
        self.common_view = CommonView()

    def register(self):
        data = self.common_view.register()
        result = self.attendee_model.register(data)        
        self.common_view.alert(result['message'])