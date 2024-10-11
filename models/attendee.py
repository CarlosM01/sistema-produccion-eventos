from user import User

class Attendee(User):
    def __init__(self, rut, nombre, email, telefono) -> None:
        super().__init__(rut, nombre, email, telefono)

    def createReservation():
        pass