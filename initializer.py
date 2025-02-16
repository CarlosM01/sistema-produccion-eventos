from models.roles import RoleModel
from models.root import RootModel

def initial_data():
    role_model = RoleModel()
    root_model = RootModel()

    # Initialize roles table
    roles = ['root', 'admin', 'attendee']
    for role in roles:
        role_model.create_role({'role_name': role})

    # Initialize super user data
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

    # Consider using some security protocol with this information before deploying to production