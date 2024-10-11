class Validations():
    def __init__(self) -> None:
        pass

    def rut():
        pass

    def intNumber(self, min, max):
        while True: 
            try:
                userInput = int(input())
                if min <= userInput <= max:
                    return userInput
                else:
                    print('Ingrese un número válido') 
            except:
                print('Debe ingresar un número')

    
    def email():
        pass

    def phoneNumber():
        pass