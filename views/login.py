class Login():
    def show():
            print('Iniciar Sesion')
            data = {
            'rut': input('Ingrese su RUT: '),
            'password': input('Ingrese su PASSWORD: '),
            }
            return(data)