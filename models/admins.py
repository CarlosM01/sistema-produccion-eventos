from models.users import UserModel

class AdminModel(UserModel):
    def __init__(self):
        super().__init__()
        self.role_id = 2

    def manage_users(self):
        pass