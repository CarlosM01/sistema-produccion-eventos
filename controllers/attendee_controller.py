from models.attendees import AttendeeModel               #Se importa la clase AttendeeModel.
from views.attendee import Attendee                      #Se importa la clase Attendee.
from views.common import Common                          #Se importa la clase Common.

class AttendeeController: #Crea la clase AttendeeController, es funciona como controlador MVC.
    def __init__(self):   #Constructor de la clase, se ejecuta para crear una instancia del controlador.
        self.attendee_model = AttendeeModel() #Crea una instancia del modelo de asistentes (AttendeeModel), para la gestionar la lógica de los mismos.
        self.attendee_view = Attendee()       #Crea una instancia de la vista (Attendee), para manejar la interfaz de los asistentes.
        self.common_view = Common()           #Crea una instancia de la vista (Common), que maneja funciones comunes como los registros y alertas.

    def register(self): #Este metodo servira para registrar asistentes
        data = self.common_view.register()             #Invoca al método "register" de la vista "Common", que recopilara datos del usuario.
        result = self.attendee_model.register(data)    #Envía los datos recopilados al modelo "AttendeeModel" para registrar al asistente en la base de datos.
        self.common_view.alert(result['message'])      #Invoca al método "alert" de la "Common" para mostrar un mensaje, basado en el resultado del registro.
