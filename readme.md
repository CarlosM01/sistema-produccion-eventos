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


notas:
* Están pendientes las verificaciones de datos de entrada
* Considerar hashear contraseñas
* Incluir opcion de cancelar envio de formularios

Diego:
* Faltan validaciones ./utils/validatios.py
* Avanzar en creacion de vistas


Diagrama de Flujo de Controladores

@startuml
start

:Inicializar ataBase;
:Inicializar MainController;
:Mostrar Main Menu;
-> Condición: ¿El usuario selecciona "Login"?;
if (Login exitoso?) then (Sí)
    :Iniciar sesión y redirigir al dashboard;
    -> Condición: ¿Usuario activo?;
    if (Rol del usuario) then (Rol: Root)
        :Mostrar menú Root;
        -> Condición: ¿Registrar nuevo usuario?;
        if (Registrar?) then (Sí)
            :Llamar a la función register;
        endif
        -> Condición: ¿Cerrar sesión?;
        if (Cerrar sesión?) then (Sí)
            :Finalizar sesión;
        endif
    elseif (Rol: Admin)
        :Mostrar alerta "Admin Dashboard";
    elseif (Rol: Attendee)
        :Mostrar alerta "Attendee Dashboard";
    else
        :Volver al Main Menu;
    endif
else (No)
    -> Condición: ¿Registrar usuario? (Desde Main Menu);
    if (Sí) then (Registrar)
        :Llamar a la función register;
        -> Condición: ¿Usuario activo?;
        if (Sí) then (Root User)
            :Registrar desde RootModel;
        else (Attendee User)
            :Registrar desde AttendeeModel;
        endif
    endif
    -> Condición: ¿Salir del sistema?;
    if (Sí) then (Salir)
        :Mostrar mensaje de salida;
        stop
    endif
endif

@enduml


Estructura de Archivos 

@startuml

package "app" {
    
    package "controllers" {
        class AdminController
        class AttendeeController
        class MainController
        class RootController
    }

    package "models" {
        class AdminsModel
        class AttendeesModel
        class CrudModel
        class LocationsModel
        class RolesModel
        class RootModel
        class SeatsModel
        class ShowsModel
        class UsersModel
    }

    package "services" {
        class SessionService
    }

    package "utils" {
        class Validations
    }

    package "views" {
        class AdminView
        class AttendeeView
        class CommonView
        class RootView
        class WelcomeView
    }
    
    class Database
    class Initializer
    class Main

}

Database --> models : "Gestiona datos"
SessionService --> controllers : "Administra sesiones"
controllers --> views : "Interactúa con"
controllers --> models : "Accede a"
utils --> views : "Soporte para validaciones"
Main --> controllers : "Inicia flujo de control"
Initializer --> Database : "Configura base de datos"

@enduml
