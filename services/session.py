class SessionModel:
    def __init__(self):
        self.active_user = None  # Almacena el usuario autenticado

    def start_session(self, user_data:dict):
        """Inicia la sesión con la información del usuario."""
        self.active_user = user_data

    def get_active_user(self) -> dict:
        """Retorna el usuario activo si hay sesión iniciada."""
        return self.active_user

    def end_session(self):
        """Termina la sesión actual."""
        self.active_user = None


#Si se necesita persistencia de datos considerar guardar la sesion en db
 