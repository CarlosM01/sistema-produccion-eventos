from models.users import UserModel

class RootModel(UserModel):
    def __init__(self):
        super().__init__()
        self.role_id = 1

    def create_admin(self):
        pass