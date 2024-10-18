from controllers.main_controller import MainController     #Importa el controlador principal "MainController".
from initializer import initial_data                       #Importa la función initial_data().

def main():                                    #Esta función ejecutara la lógica principal del sistema
    initial_data()                             #Invoca la esta función para asegurar que la base de datos se ejecuta correctamente.
    main_controller = MainController()         #Esta intancia creada gestionará el flujo principal de la aplicación.
    main_controller.start()                    #Invoca el este método para iniciar el ciclo principal del programa, para que el usuario interactue con los menús y funcionalidades.
    
    
if __name__ == "__main__":                    #Verifica que todo se ejecute correctamente llamando a "main".
    main()
