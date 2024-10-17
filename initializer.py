from models.roles import RoleModel
from models.root import RootModel

def initial_data():
    role_model = RoleModel()
    root_model = RootModel()

    # Inicializando tabla de roles 
    roles = ['root', 'admin', 'attendee']
    for role in roles:
        role_model.create_role({'role_name': role})

    # Inicializando datos de super usuario
    sudo_email = 'root@email.com'
    existing_user = root_model.get_by_attribute('email', sudo_email)
    if not existing_user:
        sudo = {
            'name': 'Super User',
            'email': sudo_email,
            'phone': '123456789',
            'password': 'root',
        }
        root_model.register(sudo)

    # Considerar usar algún protocolo de seguridad con esta información antes de desplegar a producción