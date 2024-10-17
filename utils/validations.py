class Validations():
    def __init__(self) -> None:
        pass

    def name():
        pass

    @staticmethod
    def int_number(min, max):
        while True: 
            try:
                user_input = int(input())
                if min <= user_input <= max:
                    return user_input
                else:
                    print('Ingrese un número válido') 
            except:
                print('Debe ingresar un número')

    @staticmethod
    def get_valid_id(req: list, action: str) -> int | None:
        """Valida la selección de un ID o permite cancelar la operación."""
        while True:
            selected_id = input(f'Seleccione el Id del usuario que desea {action.upper()} o "X" para cancelar: ')
            if selected_id.strip().upper() == 'X':
                print('Operación cancelada')
                return None  # Operación cancelada

            try:
                selected_id = int(selected_id)
            except:
                print('Debe ingresar un número válido.')
                continue

            if selected_id in req:
                return selected_id  # ID válido
            else:
                print('Seleccione un ID válido.')

    
    def email():
        pass

    def phone_number():
        #Se podria usar un try except, y la funcion int()
        pass

    def password():
        pass