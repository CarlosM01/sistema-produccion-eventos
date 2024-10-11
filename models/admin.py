from user import User

class Admin(User):
    def __init__(self, rut, nombre, email, telefono) -> None:
        super().__init__(rut, nombre, email, telefono)

    def createShow():
        pass