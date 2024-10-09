class Validations():
    def __init__(self) -> None:
        pass

    def rut():
        pass

    def intNumber(min, max):
        try:
            while True: 
                userInput = int(input())
                if min-1 < userInput < max+1:
                    return userInput
                else:
                    print('Ingrese un número válido') 
        except:
            print('Debe ingresar un número')

    

    def email():
        pass

    def phoneNumber():
        pass