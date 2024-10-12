from utils.validations import Validations


class Welcome():
    def __init__(self):
        self.v = Validations()

    def menu(self) -> int:
        print('''
Bienvenido/a al sistema de gestión de eventos
    SELECCIONE UNA OPCIÓN:
    1. Iniciar sesión
    2. Registrar usuario
    3. Salir
''')
        option = self.v.int_number(1,3) 
        return (option)
        
    def login(self) ->dict:
        print('Iniciar Sesion')
        data = {
        'email': input('Ingrese su EMAIL: '),
        'password': input('Ingrese su PASSWORD: '),
        }
        return(data)
    
