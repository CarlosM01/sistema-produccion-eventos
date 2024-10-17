from tabulate import tabulate

from utils.validations import Validations

from views.common import CommonView

class RootView(CommonView):    
    def __init__(self):
        super().__init__()
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
    

    def update_admin(self, req:list) ->int:
        print('---Actualizar Datos de Administrador---')

        while True:
            selected_id = input('Seleccione el Id del usuario que desea modificar o "X" para cancelar')
            if int(selected_id) in req:
                data = self.update_user()
                return [selected_id, data]
            elif selected_id.upper == 'X':
                return None
            else: print('Seleccione un id válido')
        

