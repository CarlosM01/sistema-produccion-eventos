class Validations():                                        #Se define la clase validaciones.
    def __init__(self) -> None:                             #Se llama al constructor de la clase.
        pass                                                #Pasa a la siguiente linea.

    def rut():                                              #Se define el método "rut" que será utilizado para validar el RUT de los usuarios.
        pass                                                #Pasa a la siguiente linea.

    @staticmethod
    def int_number(min, max):                               #Define el método int_numer(), toma los parametros "min" y "max" para representar los limites de la validación de números enteros. 
        while True:                                         #Inicia un bucle infinito hasta que la validación sea exitosa. 
            try:                                            #Se utiliza try para convertir lo que reciba del usuario en un número entero.
                user_input = int(input())
                if min <= user_input <= max:                #Si el número ingresa esta dentro del rango, devuelve el valor y el bucle se detiene.
                    return user_input
                else:                                       #Si el número ingresa no esta dentro del rango, el bucle continua.
                    print('Ingrese un número válido') 
            except:
                print('Debe ingresar un número')

    
    def email():                                           #Define un método que se utilizara para validar direcciones de correo electrónico.
        pass

    def phone_number():                                    #Define un método que se utilizara para validar los números de teléfono.                          
    pass
