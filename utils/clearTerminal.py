import os                         #Importa el modulo "os".

def clear_terminal():             #Define la función capaz de limpiar la terminal.
    # Windows                     
    if os.name == 'nt':           #Se agrega para identificar el nombre del sistema operativo, si es windows, "os.name" devuelve "nt".
        os.system('cls')          #Si el sistema es windows se ejecuta el comando "cls" usando "os.system()" que limpia la terminal
    # Unix/Linux/Mac            
    else:                         #Si el sistema operativo es Unix, Linux o Mac, se ejecutara lo siguiente:
        os.system('clear')        #El comando "clear" limpiara la terminal de estos sistemas operativos.

