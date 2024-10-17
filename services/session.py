class Session:
    _instance = None  # Almacena la única instancia de la clase

    #pantron Singleton, asegura que la clase solo se instancie una vez
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.active_user = None
        return cls._instance

    def start_session(self, user_data: dict):
        """Inicia la sesión con la información del usuario."""
        self.active_user = user_data

    def get_active_user(self) -> dict:
        """Retorna el usuario activo si hay sesión iniciada."""
        return self.active_user

    def end_session(self):
        """Termina la sesión actual."""
        self.active_user = None



#Si se necesita persistencia de datos considerar guardar la sesion en db
 