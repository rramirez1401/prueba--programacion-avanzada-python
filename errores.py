import datetime
import pytz

tz_CL = pytz.timezone('America/Santiago')
datetime_CL = datetime.datetime.now(tz_CL)

ruta_log = "error.log"


##DEFINO LOS ERRORES, EL MENSAJE POR DEFECTO QUE ENTREGA Y LA CONFIGURACION NECESARIA PARA INGRESARLA EN EL ARCHIVO ERROR.LOG
class Error(Exception):
    def __init__(self, mensaje="Ha ocurrido un error"):
        self.timestamp = datetime.datetime.now(pytz.timezone('America/Santiago'))
        self.nombre_error = self.__class__.__name__
        self.mensaje = mensaje
        with open(ruta_log, "a+", encoding="utf-8") as log:
            log.write(f"{self.timestamp.strftime('%d/%m/%Y %H:%M:%S')} - {self.nombre_error}: {self.mensaje}\n")
        super().__init__(mensaje)

class LargoExcedidoError(Error):
    def __init__(self, mensaje="Nombre excede los 250 caracteres"):
        super().__init__(mensaje)

class SubTipoInvalidoError(Error):
    def __init__(self):
        mensaje = "Subtipo ingresado no es válido"
        super().__init__(mensaje)
