from models.roles import RoleModel
from models.root import RootModel
from utils.validations import Validations

role_model = RoleModel()
root_model = RootModel()
v = Validations()

def initial_data():
    print('''Bienvenido/a al sistema de gestión de eventos.
Antes de comenzar debemos configurar los datos de administrador principal:
''')
    email = v.email('Crear Email:  ')

    while True:
        password = v.password('Crear contraseña:  ')
        pass_confirm = input('Confirmar contraseña:  ')
        if password == pass_confirm: 
            break
        else: print('Las contraseñas no coinciden, intente nuevamente:  ')
    # Inicializando tabla de roles 
    roles = ['root', 'admin', 'attendee']
    for role in roles:
        role_model.create_role({'role_name': role})

    # Inicializando datos de super usuario 
    sudo = {
        'name': 'Super User',
        'email': email,
        'phone': '123456789',
        'password': password
    }
    root_model.register(sudo)

def start_initializer():
    if not root_model.get_all():
        initial_data()

    # Considerar usar algún protocolo de seguridad con esta información antes de desplegar a producción