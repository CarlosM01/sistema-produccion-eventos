from models.roles import Role
from models.users import User

def initial_data():
    role_model = Role()
    user_model = User()

    roles = ['root', 'admin', 'attendee']
    for role in roles:
        existing_role = role_model.get_by_name(role)
        if not existing_role:
            role_model.post(role)

    sudo_email = 'admin@example.com'
    existing_user = user_model.get_by_email(sudo_email)
    if not existing_user:
        sudo = {
            'name': 'Super User',
            'email': sudo_email,
            'phone': '123456789',
            'password': 'admin'
        }
        user_model.post(sudo)