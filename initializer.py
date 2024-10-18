from models.roles import RoleModel            #Importa la clase "RoleModel".
from models.root import RootModel             #Importa la clase "RootModel".

def initial_data():                           #Esta función agrega a la base de datos con datos iniciales.
    role_model = RoleModel()                  #Crea un instancia llamada "RoleModel" para luego interactuar con las tablas en la base de datos.
    root_model = RootModel()                  #Crea un instancia llamada "RootModel" para luego interactuar con las tablas en la base de datos

    roles = ['root', 'admin', 'attendee']     #Define una lista de roles que seran añadidos a la tabla "roles".
    for role in roles:                        #Itera sobre la lista de roles: 
        role_model.create_role({'role_name': role}) #Para agregar cada rol en la base de datos, si no existe.

    sudo_email = 'root@example.com'           #Defien el email del superusuario "root", para verificar si ya existe un usuario ya registrado.
    existing_user = root_model.get_by_attribute('email', sudo_email)  #Busca en la base de datos si existe el usuario.
    if not existing_user:                     #Si no existe entonces, se procede a registrar uno nuevo.
        sudo = {
            'name': 'Super User',
            'email': sudo_email,
            'phone': '123456789',
            'password': 'root',
        }
        root_model.register(sudo)            #Utiliza el método "register" para registrar al nuevo usuario "root" y se guarda en la base de datos.
