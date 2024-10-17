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
        id = self.v.get_valid_id(req, 'Actualizar')
        if id:
            data = self.update_user()
            print('Usuario ACTUALIZADO')
            return {'succes':True, 'id':id, 'data':data}
        else: return {'succes': False}


    def delete_admin(self, req:list):
        print('---Eliminar Datos de Administrador---')
        id = self.v.get_valid_id(req, 'Eliminar')
        if id:
            print('Usuario ELIMINADO')
            return {'succes':True, 'id':id}
        else: return {'succes': False}

    def manage_admin_action(self, req: list, action: str) -> dict:
        """Método genérico para actualizar o eliminar un administrador."""
        print(f'---{action.capitalize()} Datos de Administrador---')

        id = self.v.get_valid_id(req, action)
        if not id:
            return {'success': False}

        if action == 'actualizar':
            data = self.update_user()
            print('Usuario ACTUALIZADO')
            return {'success': True, 'id': id, 'data': data}

        elif action == 'eliminar':
            print('Usuario ELIMINADO')
            return {'success': True, 'id': id}
        
        
    def update_admin(self, req: list) -> dict:
        return self.manage_admin_action(req, 'actualizar')

    def delete_admin(self, req: list) -> dict:
        return self.manage_admin_action(req, 'eliminar')


