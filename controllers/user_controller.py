from models.users import User
from views.welcome import Welcome
from views.alert import alert

class UserController:
    def __init__(self):
        self.user = User()
        self.welcome_view = Welcome()

    def register(self):
        data = self.welcome_view.register()
        result = self.user.post(data)        
        alert(result['message'])

    def login(self):
        data = self.welcome_view.login()
        result = self.user.get_by_email(data['email'])
        if result:
            if result['password'] == data['password']:
                alert('Iniciar sesion... ')
            else: alert('Contraseña incorrecta')
        else: alert('Este email no se encuentra registrado')