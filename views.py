from utils.validations import Validations


class Views():
    def __init__(self):
        self.v = Validations()

    def welcome(self) -> str:
        print('''Bienvenido/a al sistema de gestión de eventos
        SELECCIONE UNA OPCIÓN:
        1. Iniciar sesión
        2. Registrar usuario
        3. Salir
        ''')
        option = self.v.intNumber(1,3) 
        return (option)
    
    def register(self) -> dict:
        print('Registrar usuario')
        name = input('Ingrese su NOMBRE: ')
        email = input('Ingrese su EMAIL: ')
        phone = input('Ingrese su TELEFONO: ')

        while True:
            password = input('Ingrese su CONTRASEÑA: ')
            passConfirm = input('Confirme su CONTRASEÑA: ')

            if password == passConfirm:
                return {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'password': password,
                }
                
            else: print('Las contraseñas no coinciden, intente nuevamente')
        
    def login(self) ->dict:
        print('Iniciar Sesion')
        data = {
        'rut': input('Ingrese su RUT: '),
        'password': input('Ingrese su PASSWORD: '),
        }
        return(data)