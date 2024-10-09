class Index:
    def __init__(self) -> None:
        pass

    def welcome():
        print('''Bienvenido/a al sistema de gestión de eventos
        SELECCIONE UNA OPCIÓN:

        1. Iniciar sesión
        2. Registrar usuario
        3. Salir
        ''')
    
    def signUp():
        print('Registrar usuario')
        data = {
        'rut': input('Ingrese su RUT: '),
        'name': input('Ingrese su NOMBRE: '),
        'email': input('Ingrese su EMAIL: '),
        'phone': input('Ingrese su TELEFONO: ')
        }
        return(data)
    #se debe validar que el usuario no este registrado previamente y tambien incorporar una funcion que verifique contrasenia


    def signIn():
        print('''Inicio de sesión:
        Ingresar:
               
        ''')