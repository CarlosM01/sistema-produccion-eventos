import re
from datetime import datetime

class Validations():
    def __init__(self):
        pass

    @staticmethod
    def name() -> str:
        """Valida que el nombre solo contenga letras y espacios."""
        while True:
            user_input = input().strip()
            if all(c.isalpha() or c.isspace() for c in user_input) and user_input:
                return user_input.capitalize()
            else:
                print('Ingrese un nombre válido (solo letras y espacios).')

    @staticmethod
    def email() -> str:
        """Valida el formato de un correo electrónico."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while True:
            user_input = input().strip()
            if re.match(email_regex, user_input):
                return user_input
            else:
                print('Ingrese un correo electrónico válido.')

    @staticmethod
    def phone_number() -> str:
        """Valida que el número de teléfono contenga solo dígitos."""
        while True:
            user_input = input().strip()
            if user_input.isdigit() and len(user_input) == 8:  # 8 dígitos
                return int(user_input)
            else:
                print('Ingrese un número de teléfono válido (8 dígitos).')

    @staticmethod
    def password() -> str:
        """Valida la fortaleza de la contraseña."""
        while True:
            user_input = input().strip()
            if (len(user_input) >= 8 and 
                any(char.isdigit() for char in user_input) and 
                any(char.isalpha() for char in user_input) and 
                any(char in '!@#$%^&*()_+' for char in user_input)):
                return user_input
            else:
                print('La contraseña debe tener al menos 8 caracteres, contener letras, números y un carácter especial.')

    @staticmethod
    def date() -> str:
        """Valida una fecha en formato AAAA:MM:DD."""
        while True:
            user_input = input().strip()
            try:
                date_obj = datetime.strptime(user_input, '%Y:%m:%d')
                return date_obj.strftime('%Y:%m:%d')  # Devuelve la fecha en el formato correcto
            except ValueError:
                print('Fecha inválida. Asegúrese de que esté en el formato AAAA:MM:DD.')


    def number(self, min: float, max: float, number_type: str) -> float:
        """Valida un número (entero o real) dentro de un rango específico."""
        while True:
            user_input = input().strip()
            try:
                if number_type == 'int':
                    value = int(user_input)
                if number_type == 'float':
                    value = float(user_input)

                if min <= value <= max:
                    return value
                else:
                    print('Ingrese un número válido dentro del rango especificado.')
            except ValueError:
                print('Debe ingresar un número válido.')
    
    def int_number(self, min: int, max: int) -> int:
        """Valida un número entero dentro de un rango específico."""
        return self.number(min, max, 'int')
    
    def float_number(self, min: float, max: float) -> float:
        """Valida un número real dentro de un rango específico."""
        return self.number(min, max, 'float')


    @staticmethod
    def get_valid_id(available_ids: list, action:str=()) -> int | None:
        """Valida la selección de un ID o permite cancelar la operación."""
        while True:
            if action:
                selected_id = input(f'Seleccione el Id que desea {action.upper()} o "X" para cancelar: ')  
            else: selected_id = input()
            
            if selected_id.strip().upper() == 'X':
                print('Operación cancelada')
                return None  # Operación cancelada

            try:
                selected_id = int(selected_id)
            except ValueError:
                print('Debe ingresar un número válido.')
                continue

            if selected_id in available_ids:
                return selected_id  # ID válido
            else:
                print('Seleccione un ID válido.')
