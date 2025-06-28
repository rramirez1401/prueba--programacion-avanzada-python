import datetime
import pytz

tz_CL = pytz.timezone('America/Santiago')
datetime_CL = datetime.datetime.now(tz_CL)

ruta_log = "error.log"


class Error(Exception):
    with open(ruta_log, "a+") as log:
                log.write(f"{datetime_CL.strftime("%d/%m/%Y %H:%M:%S")}, {Exception} \n")

class LargoExcedidoError(Error):
    print("jajajaja")

class SubTipoInvalidoError(Error):
    pass