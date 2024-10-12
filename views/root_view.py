from utils.validations import Validations
from tabulate import tabulate


class RootView:    
    def __init__(self):
        self.v = Validations()


    def menu(self):
        print('''
Bienvenido/a SueperUser

SELECCIONE UNA OPCIÓN:
    1. Ver Administradores
    2. Crear Administrador
    3. Actualizar datos de Administrador
    4. Eliminar Administrador
    5. Volver al menú principal
    6. Salir de la aplicación
''')
        option = self.v.int_number(1, 6)
        return(option)
    

    def display_admins(self, data):
        if not data:
            print("No hay datos disponibles.")
            return
        
        print(tabulate(data, headers="keys", tablefmt="pretty"))
    


