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
    

    def manage_admin_action(self, available_ids: list, action: str) -> dict:
        """Método genérico para actualizar o eliminar un administrador."""
        print(f'---{action.capitalize()} Datos de Administrador---')

        id = self.v.get_valid_id(available_ids, action)
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


