from views.common import CommonView

class AttendeeView(CommonView):    
    def __init__(self):
        super().__init__()


    def menu(self, user_name:str)->int:
        print(f'''
Bienvenido/a {user_name}

SELECCIONE UNA OPCIÓN:
    1. Nueva reserva
    2. Ver mis reservas
    3. Anular reserva
    4. Actualizar información personal
    5. Volver al menú principal
    6. Salir de la aplicación
''')
        option = self.v.int_number(1, 6)
        return(option)

    

    def buy_ticket(self, details) ->int:
        available_seats = details['capacity'] - details['reservations']
        if available_seats == 0:
            print('No quedan cupos para este evento')
            return False
        
        print(f'Quedan {available_seats} asientos disponibles de {details['capacity']}')
        if input(f'¿Desea comprar un boleto para {details['name']}? (S/N):  ').upper().strip() != 'S':
            print('Operación cancelada')
            return False
        
        if input(f'El total a pagar es ${details['price']}.  ¿Confirmar pago?  (S/N):  ').upper().strip() != 'S':
            print('Compra anulada')
            return False
        print('Pago realizado')
        return True
    

    def display_ticket(self, data):
        print('¡Gracias por su compra!')
        self.display(data)
        input('Preseione ENTER para continuar')

    def delete_reservation(self):
        if input('¿Eliminar reserva? (S/N)  ').upper().strip() != 'S':
            return False
        return True
        
        
        
