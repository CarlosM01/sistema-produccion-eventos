from controllers.main_controller import MainController
from initializer import initial_data

def main():
    initial_data()
    main_controller = MainController()
    main_controller.start()
    
    
if __name__ == "__main__":
    main()