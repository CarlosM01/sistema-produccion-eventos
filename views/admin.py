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
    3. Volver
''')
        option = self.v.int_number(1, 3)
        return(option)
    

    def select_location(self, available_ids:list)->int:
        print('Seleccione la Id de la sede:')
        id = self.v.get_valid_id(available_ids)
        if id:
            return {'success':True, 'id':id}  
        else: return {'success':False}
    

    def create_location(self)->dict:
        print('---CREAR SEDE---')
        print('')
        print('Nombre de la sede:  ')
        name = self.v.name()
        print('Dirección:  ')
        address = self.v.name()
        print('Capacidad:  ')
        capacity = self.v.int_number(1,1000)

        return {'name':name, 'address':address, 'capacity':capacity}


    def create_show(self)->dict:
        print('---CREAR EVENTO---')
        print('')
        print('Nombre del evento:  ')
        name = self.v.name()
        print('Artista:  ')
        artist = self.v.name()
        print('Descrición:  ')
        description = self.v.name()
        print('Fecha (AAAA/MM/DD):  ')
        date = self.v.date()
        print('Precio:  ')
        price = self.v.float_number(1,1000000)

        return {'name':name, 'artist':artist, 'description':description, 'date':date, 'price':price}


    def select_show(self, available_ids):
        print('Si desea ver los detalles de un evento seleccione el ID, para cancelar ingrese "X"  ')
        id = self.v.get_valid_id(available_ids)
        if id:
            return {'success':True, 'id':id}  
        else: return {'success':False}
        