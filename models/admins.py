from models.users import UserModel

class AdminModel(UserModel):
    def __init__(self):
        super().__init__()
        self.role_id = 2

    def get_admin_list(self):
        self.db.connect()
        result = self.db.SQL(f"SELECT user_id, name, email, phone FROM {self.table_name} WHERE role_id = {self.role_id}")
        self.db.close()
        return result
    
    