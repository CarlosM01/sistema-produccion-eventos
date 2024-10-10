import os

def clear_terminal():
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Unix/Linux/Mac
    else:
        os.system('clear')

