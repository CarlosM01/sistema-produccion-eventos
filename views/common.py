class Common():
    def register(self) -> dict:
        print('Registrar usuario')
        name = input('Ingrese su NOMBRE: ')
        email = input('Ingrese su EMAIL: ')
        phone = input('Ingrese su TELEFONO: ')

        while True:
            password = input('Ingrese su CONTRASEÑA: ')
            pass_confirm = input('Confirme su CONTRASEÑA: ')

            if password == pass_confirm:
                return {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'password': password
                }
                
            else: print('Las contraseñas no coinciden, intente nuevamente')

    @staticmethod
    def alert(message):
        print(message)