from controllers.main_controller import MainController
from initializer import initial_data

def main():
    initial_data()
    main_controller = MainController()
    main_controller.redirect_to_dashboard()
    
#Punto de partida de la aplicación    
if __name__ == "__main__":
    main()



# Este archivo comienza el flujo de ejecución de la aplicación.
# La funcion principal se encarga de llamar al inicializador de datos 
# Luego se ejecuta el controlador principal