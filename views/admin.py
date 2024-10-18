from tabulate import tabulate

from utils.validations import Validations

from views.common import CommonView

class AdminView(CommonView):    
    def __init__(self):
        super().__init__()
        self.v = Validations()


    def menu(self, user_name:str)->int:
        print(f'''
Bienvenido/a {user_name}

SELECCIONE UNA OPCIÓN:
    1. Administrar sedes
    2. Crear Evento
    3. Ver eventos disponibles 
    4. Actualizar Información de evento
    5. Eliminar evento
    6. Actualizar información personal
    7. Volver al menú principal
    8. Salir de la aplicación
''')
        option = self.v.int_number(1, 8)
        return(option)


    def locations_menu(self):
        print(f'''
---SEDES---
SELECCIONE UNA OPCIÓN:
    1. Ver sedes
    2. Registrar sede
    3. Editar sede
    4. Eliminar Sede
    5. Volver
''')
        option = self.v.int_number(1, 5)
        return(option)
    

    def select_location(self, available_ids:list)->dict:
        id = self.v.get_valid_id(available_ids, 'Seleccione la Id de la sede, para cancelar ingrese "X"  ')
        if id:
            return {'success':True, 'id':id}  
        else: return {'success':False}
    

    def create_location(self)->dict:
        print('---CREAR SEDE---')
        data =  {
            'name': self.v.name('Nombre de la sede:  '),
            'address': input('Dirección:  '),
            'capacity': self.v.int_number(1,1000,'Capacidad:  ')
        }
        return data
    

    def update_location(self, available_ids) -> dict:
        print('---ACTUALIZAR SEDE---')

        id = self.v.get_valid_id(available_ids, 'Seleccione la ID de la sede que desea ACTUALIZAR, para cancelar ingrese "X":  ')
        if not id:
            return {'success':False}

        inputs =  {
            'name': self.v.name('Nombre de la sede (Dejar en blanco para omitir):  ', True),
            'address': input('Dirección  (Dejar en blanco para omitir):  '),
            'capacity': self.v.int_number(1,1000,'Capacidad  (Dejar en blanco para omitir):  ', True)
        }
        data = {key: value for key, value in inputs.items() if value}
        if not data:
            print('No se realizaron cambios')
            return {'success':False}
        
        print('Sede ACTUALIZADA')
        return {'success': True, 'id': id, 'data': data}
    
    def delete_location(self, available_ids):
        id = self.v.get_valid_id(available_ids, 'Seleccione la Id de la sede que desea ELIMINAR, para cancelar ingrese "X"  ')
        confirm = input('¡ADVERTENCIA! Se eliminaran los eventos asociados a esa Sede, desea continuar  (S/N):  ')
        if id and confirm.upper().strip()=='S':
            print('Sede Eliminada')
            return {'success':True, 'id':id}  
        else: return {'success':False}


    def create_show(self)->dict:
        print('---CREAR EVENTO---')
        data = {
            'name': input('Nombre del evento:  ').strip(),
            'artist': input('Artista:  ').strip(),
            'description': input('Descrición:  ').strip(),
            'date': self.v.date('Fecha (AAAA:MM:DD):  '),
            'price': self.v.float_number(1,1000000, 'Precio:  ')
        }
        return data


    def select_show(self, available_ids):
        id = self.v.get_valid_id(available_ids, 'Si desea ver los detalles de un evento seleccione el ID, para cancelar ingrese "X"  ')
        if id:
            return {'success':True, 'id':id}  
        else: return {'success':False}

        
    def update_show(self, available_ids: list) -> dict:
        print('--- Actualizar Datos ---')
        id = self.v.get_valid_id(available_ids, 'Seleccione el ID del evento que desea ACTUALIZAR, para cancelar ingrese "X"  ')
        if not id:
            return {'success': False}
        
        inputs = {
            'name': input('Ingrese nuevo NOMBRE (Dejar en blanco para omitir): ').strip(),
            'artist': input('Ingrese nuevo ARTISTA (Dejar en blanco para omitir): ').strip(),
            'description': input('Ingrese nueva DESCRIPCIÓN (Dejar en blanco para omitir): ').strip(),
            'date': self.v.date('Ingrese nueva FECHA (Dejar en blanco para omitir): ', True),
            'price': self.v.float_number(1,1000000, 'Ingrese nuevo PRECIO (Dejar en blanco para omitir): ', True)
        }     

        # Crear diccionario solo con los campos no vacíos
        data = {key: value for key, value in inputs.items() if value}
        if not data:
            print('No se realizaron cambios')
            return {'success': False}
        
        print('evento ACTUALIZADO')
        return {'success': True, 'id': id, 'data': data}
    

    def update_location_show(self, available_ids):
        option = input('¿Desea cambiar la ubicación del evento? S/N  ')
        if option.upper().strip() == 'S':
            id = self.v.get_valid_id(available_ids, 'Seleccione la ID de la nueva Sede, para cancelar ingrese "X"  ')
            if id: 
                return {'success':True, 'id':id}
        return {'success':False}


    def delete_show(self, available_ids: list) -> dict:
        print('--- Eliminar Datos ---')
        id = self.v.get_valid_id(available_ids, 'Seleccione el ID del evento que desea ELIMINAR, para cancelar ingrese "X"  ')
        if not id:
            return {'success': False}
        print('evento ELIMINADO')
        return {'success': True, 'id': id}
    

    def update_password(self, current_password):
        if input('¿Desea actualizar contraseña? (S/N): ').strip().upper() != 'S':
            return None  # No se actualiza la contraseña

        if input('Ingrese su contraseña actual: ') != current_password:
            print('Contraseña incorrecta')
            return None

        while True:
            new_password = self.v.password('Escriba su nueva contraseña: ')
            if new_password == input('Confirme su nueva contraseña: '):
                print('Contraseña actualizada exitosamente')
                return new_password
            print('Las contraseñas no coinciden, intente nuevamente')
