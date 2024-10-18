import re
from datetime import datetime

class Validations:
    def __init__(self):
        pass

    @staticmethod
    def name(info: str = '', allow_empty: bool = False) -> str | None:
        """Valida que el nombre solo contenga letras y espacios."""
        while True:
            user_input = input(info).strip()
            if allow_empty and not user_input:
                return None
            if all(c.isalpha() or c.isspace() for c in user_input) and user_input:
                return user_input.capitalize()
            print('Ingrese un nombre válido (solo letras y espacios).')

    @staticmethod
    def email(info: str = '', allow_empty: bool = False) -> str | None:
        """Valida el formato de un correo electrónico."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        while True:
            user_input = input(info).strip()
            if allow_empty and not user_input:
                return None
            if re.match(email_regex, user_input):
                return user_input
            print('Ingrese un correo electrónico válido.')

    @staticmethod
    def phone_number(info: str = '', allow_empty: bool = False) -> int | None:
        """Valida que el número de teléfono contenga solo dígitos."""
        while True:
            user_input = input(info).strip()
            if allow_empty and not user_input:
                return None
            if user_input.isdigit() and len(user_input) == 8:
                return int(user_input)
            print('Ingrese un número de teléfono válido (8 dígitos).')

    @staticmethod
    def password(info: str = '', allow_empty: bool = False) -> str | None:
        """Valida la fortaleza de la contraseña."""
        while True:
            user_input = input(info).strip()
            if allow_empty and not user_input:
                return None
            if (len(user_input) >= 8 and 
                any(char.isdigit() for char in user_input) and 
                any(char.isalpha() for char in user_input) and 
                any(char in '!@#$%^&*()_+' for char in user_input)):
                return user_input
            print('La contraseña debe tener al menos 8 caracteres, contener letras, números y un carácter especial.')

    @staticmethod
    def date(info: str = '', allow_empty: bool = False) -> str | None:
        """Valida una fecha en formato AAAA:MM:DD."""
        while True:
            user_input = input(info).strip()
            if allow_empty and not user_input:
                return None
            try:
                date_obj = datetime.strptime(user_input, '%Y:%m:%d')
                return date_obj.strftime('%Y:%m:%d')
            except ValueError:
                print('Fecha inválida. Asegúrese de que esté en el formato AAAA:MM:DD.')

    def number(self, min: float, max: float, number_type: str, info: str = '', allow_empty: bool = False) -> float | None:
        """Valida un número dentro de un rango específico."""
        while True:
            user_input = input(info).strip()
            if allow_empty and not user_input:
                return None
            try:
                value = int(user_input) if number_type == 'int' else float(user_input)
                if min <= value <= max:
                    return value
                print('Ingrese un número válido dentro del rango especificado.')
            except ValueError:
                print('Debe ingresar un número válido.')

    def int_number(self, min: int, max: int, info: str = '', allow_empty: bool = False) -> int | None:
        """Valida un número entero dentro de un rango específico."""
        return self.number(min, max, 'int', info, allow_empty)

    def float_number(self, min: float, max: float, info: str = '', allow_empty: bool = False) -> float | None:
        """Valida un número real dentro de un rango específico."""
        return self.number(min, max, 'float', info, allow_empty)

    @staticmethod
    def get_valid_id(available_ids: list, info: str = '', allow_empty: bool = False) -> int | None:
        """Valida la selección de un ID o permite cancelar la operación."""
        while True:
            user_input = input(info).strip()
            if allow_empty and not user_input:
                return None
            if user_input.upper() == 'X':
                print('Operación cancelada')
                return None
            try:
                selected_id = int(user_input)
                if selected_id in available_ids:
                    return selected_id
                print('Seleccione un ID válido.')
            except ValueError:
                print('Debe ingresar un número válido.')
