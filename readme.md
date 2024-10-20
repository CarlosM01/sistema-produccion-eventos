# Sistema de Gestión de Eventos

La aplicación sigue la arquitectura MVC para mantener la separación de responsabilidades.

**Lenguaje:**
    
- Python 3.12.5

**Dependencias:**
    
- tabulate==0.9.0


## Instrucciones de Instalación

1. **Clona el repositorio:** 

    ```bash
    git clone https://github.com/CarlosM01/sistema-produccion-eventos.git
    cd sistema-gestion-eventosS
2. **Instala las dependencias del proyecto**
    ```bash
    pip install -r requirements.txt
3. **Iniciar la aplicación**
    ```bash
    python3 main.py
___


**notas:**
* La aplicacion actualmente es vulnerable a Inyeccion de SQL
* Considerar hashear contraseñas
* considerar incluir opcion de cancelar envio de formularios
* AttendeeController no esta optimizado
* Hay algunos patrones de disenio inconsistentes
* El envio de informacion entre componentes no esa estandarizado (considerar usar solo diccionarios)