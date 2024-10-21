from models.users import UserModel

class AttendeeModel(UserModel):
    def __init__(self):
        super().__init__()
        self.role_id = 3
        