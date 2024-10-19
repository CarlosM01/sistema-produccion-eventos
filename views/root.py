from views.common import CommonView

class RootView(CommonView):    
    def __init__(self):
        super().__init__()


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
    

    def update_admin(self, available_ids: list) -> dict:
        id = self.v.get_valid_id(available_ids)
        if not id:
            return {'success': False}
        data = self.update_user()
        print('Usuario ACTUALIZADO')
        return {'success': True, 'id': id, 'data': data}


    def delete_admin(self, available_ids: list) -> dict:
        id = self.v.get_valid_id(available_ids)
        if not id:
            return {'success': False}
        print('Usuario ELIMINADO')
        return {'success': True, 'id': id}

