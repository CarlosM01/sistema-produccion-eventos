from models.roles import Role
from models.root import RootModel

def initial_data():
    role_model = Role()
    root_model = RootModel()

    roles = ['root', 'admin', 'attendee']
    for role in roles:
        existing_role = role_model.get_by_name(role)
        if not existing_role:
            role_model.post(role)

    sudo_email = 'root@example.com'
    existing_user = root_model.get_by_attribute('email', sudo_email)
    if not existing_user:
        sudo = {
            'name': 'Super User',
            'email': sudo_email,
            'phone': '123456789',
            'password': 'root',
        }
        root_model.post(sudo)