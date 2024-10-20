from controllers.main import MainController
from initializer import start_initializer

def main():
    start_initializer()
    main_controller = MainController()
    main_controller.redirect_to_dashboard()
    
#Punto de partida de la aplicación    
if __name__ == "__main__":
    main()