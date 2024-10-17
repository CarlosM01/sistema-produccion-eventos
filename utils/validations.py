class Validations():
    def __init__(self) -> None:
        pass

    def name():
        pass

    def rut():
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
    
    def email():
        pass

    def phone_number():
        #Se podria usar un try except, y la funcion int()
        pass

    def password():
        pass