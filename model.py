class Evento():
    def __init__(self) -> None:
        self.lugar
        self.date
        self.capacity

class Asiento():
    pass

class Persona():
    def __init__(self, rut, nombre, email, telefono) -> None:
        self.rut = rut
        self.nombre = nombre
        self.email = email
        self.telefono = telefono


class Asistente(Persona):
    def __init__(self, rut, nombre, email, telefono) -> None:
        super().__init__(rut, nombre, email, telefono)
         

class Admin(Persona):
    def __init__(self, rut, nombre, email, telefono) -> None:
        super().__init__(rut, nombre, email, telefono)
