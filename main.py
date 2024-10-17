from controllers.main import MainController
from initializer import initial_data

def main():
    initial_data()
    main_controller = MainController()
    main_controller.redirect_to_dashboard()
    
#Punto de partida de la aplicación    
if __name__ == "__main__":
    main()
 