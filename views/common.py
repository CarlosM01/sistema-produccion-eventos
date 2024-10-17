class CommonView():
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

    def update_user(self) -> dict:
        print('--- Actualizar Datos ---')

        name = input('Ingrese nuevo NOMBRE: (Dejar en blanco para omitir) ')
        email = input('Ingrese nuevo EMAIL: (Dejar en blanco para omitir) ')
        phone = input('Ingrese nuevo TELEFONO: (Dejar en blanco para omitir) ')

        # Las contraseñas deberían tener su propio sistema para actualizar
        inputs = {
            'name': name.strip(),
            'email': email.strip(),
            'phone': phone.strip()
        }

        # Crear diccionario solo con los campos no vacíos
        data = {key: value for key, value in inputs.items() if value}
        return data


    @staticmethod
    def alert(message):
        print(message)