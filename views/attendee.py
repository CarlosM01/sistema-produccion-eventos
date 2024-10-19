from views.common import CommonView

class AttendeeView(CommonView):    
    def __init__(self):
        super().__init__()


    def menu(self, user_name:str)->int:
        print(f'''
Bienvenido/a {user_name}

SELECCIONE UNA OPCIÓN:
    1. Ver eventos disponibles 
    2. Administrar mis reservas
    3. Actualizar información personal
    4. Volver al menú principal
    5. Salir de la aplicación
''')
        option = self.v.int_number(1, 5)
        return(option)
    
    def buy_ticket(self, available_seats:int):
        print(f'Quedan {available_seats} asientos disponibles')
        if input('¿Desea comprar un boleto para este evento? (S/N):  ').upper().strip() != 'S':
            return
        
        
        
        
