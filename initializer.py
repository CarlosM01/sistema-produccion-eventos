from models.roles import RoleModel
from models.root import RootModel

def initial_data():
    role_model = RoleModel()
    root_model = RootModel()

    roles = ['root', 'admin', 'attendee']
    for role in roles:
        role_model.create_role({'role_name': role})

    sudo_email = 'root@example.com'
    existing_user = root_model.get_by_attribute('email', sudo_email)
    if not existing_user:
        sudo = {
            'name': 'Super User',
            'email': sudo_email,
            'phone': '123456789',
            'password': 'root',
        }
        root_model.register(sudo)