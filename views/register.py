class Register():
    def show():
            print('Registrar usuario')
            data = {
            'rut': input('Ingrese su RUT: '),
            'name': input('Ingrese su NOMBRE: '),
            'email': input('Ingrese su EMAIL: '),
            'phone': input('Ingrese su TELEFONO: ')
            }
            return(data)
        