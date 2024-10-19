from utils.validations import Validations
from tabulate import tabulate

class CommonView():
    def __init__(self):
        self.v = Validations()

    def register(self) -> dict:
        print('---Registrar usuario---')
        name = self.v.name('Ingrese su NOMBRE: ')
        email = self.v.email('Ingrese su EMAIL: ')
        phone = self.v.phone_number('Ingrese su TELEFONO: ')

        while True:
            password = self.v.password('Ingrese su CONTRASEÑA: ')
            pass_confirm = input('Confirme su CONTRASEÑA: ')

            if password == pass_confirm:
                return {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'password': password
                }
                
            else: print('Las contraseñas no coinciden, intente nuevamente')

    def update_user(self) -> dict:
        print('---Actualizar Datos de Usuario---')
        # Las contraseñas deberían tener su propio sistema para actualizar
        inputs = {
            'name': self.v.name('Ingrese nuevo NOMBRE: (Dejar en blanco para omitir) ', True),
            'email': self.v.email('Ingrese nuevo EMAIL: (Dejar en blanco para omitir) ', True),
            'phone': self.v.phone_number('Ingrese nuevo TELEFONO: (Dejar en blanco para omitir) ', True)
        }

        # Crear diccionario solo con los campos no vacíos
        data = {key: value for key, value in inputs.items() if value}
        return data
    

    def select_show(self, available_ids):
        id = self.v.get_valid_id(available_ids, 'Si desea ver los detalles de un evento seleccione el ID, para cancelar ingrese "X"  ')
        if id:
            return {'success':True, 'id':id}  
        else: return {'success':False}
    

    def display(self, data):
        if not data:
            print("No hay datos disponibles.")
            return
        
        print(tabulate(data, headers="keys", tablefmt="pretty"))


    @staticmethod
    def exit_system():
        if input('¿Deseas salir? (S/N):  ').upper().strip() == 'S':
            print('Saliendo del Sistema')
            return True
    
    @staticmethod
    def log_out():
        if input('¿Deseas cerrar sesión? (S/N):  ').upper().strip() == 'S':
            print('Cerrando Sesión')
            return True

    @staticmethod
    def alert(message):
        print(message)