from datetime import datetime
from campania import Campania
from anuncio import Anuncio, Video, Display, Social 
from errores import LargoExcedidoError, SubTipoInvalidoError


# ESTE SCRIPT DEMO PERMITE INSTANCIAR LA CLASE CAMPANIA INGRESANDO EL NOMBRE Y LAS FECHAS REQUERIDAS CONTANDO CON LA FUNCION CREAR_CAMPANIA
# ADEMAS CUENTA CON LA FUNCION AGREGAR ANUNCIO PARA QUE AL MOMENTO DE INSTANCIAR LA CAMPAÑA AUTOMATICAMENTE LLAME A ESTA FUNCION PARA INCLUIR
# LOS DATOS REQUERIDOS PARA CREAR EL PRIMER ANUNCIO.
# POSTERIORMENTE SE EJECUTA LA FUNCION MENU_PRINCIPAL EN DONDE SE OFRECE LA OPCION DE AGREGAR MAS ANUNCIOS, MODIFICAR EL NOMBRE DE LA CAMPAÑA,
# VISUALIZAR LOS DATOS DE LA CAMPAÑA Y VISUALIZAR LOS TIPOS Y FORMATOS DE LOS ANUNCIOS


## DEFINO LA FUNCION AGREAGAR ANUNCIO QUE CONSULTA AL USUARIO EL TIPO DE ANUNCIOA A Y PREGUNTA TODOS LOS DATOS REQUERIDOS, ADEMAS TIENE UNA
#  EL PARAMETRO "CREACION" EL CUAL DEFINE SI ES PRIMERA VEZ QUE SE LLAMA A LA FUNCION, ESTO HACE QUE SOLO PIDA AGRAGAR UN SOLO ANUNCIO Y AL
#  CREAR UNA INSTANCIA DE CAMAPAÑA SE LLAMA AL METODO COMPONER_ANUNCIO QUE AGREGA ESTE ANUNCIO A LA LISTA EN EL CONSTRUCTOR DE CAMPAÑA. SI EL
#  PARAMETRO CREACIÓN ES FALSE, EL METODO COMPONER_ANUNCIO DE LA CLASE CAMPAÑA SOLO HARÁ UN APPEND CON EL ANUNCIO CREADO.
def agregar_anuncio(creacion=False):
    while True:
        datos_anuncio = []
        print("""
    Que clase de anuncio quieres agregar?

1. Video
2. Display
3. Social""")
        if not creacion:
            print("4. Salir")

        try:
            opcion = int(input("\n    >>> "))
            if not creacion and opcion == 4:
                return "salir"
            if opcion not in [1, 2, 3]:
                continue

            datos_anuncio.append(opcion)

            if opcion != 1:
                datos_anuncio.append(int(input("Ingresa el ancho:\n\n        >>> ")))
                datos_anuncio.append(int(input("Ingresa el alto:\n\n        >>> ")))
            else:
                datos_anuncio.append(1)
                datos_anuncio.append(1)

            datos_anuncio.append(input("Ingresa el url del archivo:\n\n        >>> "))
            datos_anuncio.append(input("Ingresa el url click:\n\n        >>> "))
            print("Ingresa el sub_tipo:")
            if opcion == 1:
                print(f"opciones disponibles: {Video.SUB_TIPOS}")
            elif opcion == 2:
                print(f"opciones disponibles: {Display.SUB_TIPOS}")
            else:
                print(f"opciones disponibles: {Social.SUB_TIPOS}")
            sub_tipo = (input("\n\n        >>> "))
            if (opcion == 1 and sub_tipo in Video.SUB_TIPOS or
                opcion == 2 and sub_tipo in Display.SUB_TIPOS or
                opcion == 3 and sub_tipo in Social.SUB_TIPOS):

                datos_anuncio.append(sub_tipo)
            else:
                raise SubTipoInvalidoError

            if opcion == 1:
                datos_anuncio.append(int(input("Ingresa la duracion del video:\n\n        >>> ")))
            else:
                datos_anuncio.append(1)

            datos_anuncio.append(creacion)
            return datos_anuncio

        except ValueError:
            input("Entrada no válida, intenta de nuevo por favor\n\nEnter para continuar...")



## DEFINO LA FUNCION CREAR_CREARCAMPANIA QUE SOLICITA LOS DATOS NECESARIOS PARA LA CREACION DE LA CAMPAÑA Y POSTERIORMENTE LLAMA A LA
#  FUNCIÓN AGREGAR_ANUNCIO PARA SOLICITAR LOS DATOS DEL PRIMER ANUNCIO A CREAR Y ENVIAR TODOS LOS DATOS AL CONSTRUCTOR DE CAMPAÑA
def crear_campana():
    nombre_campania = input("Elige un nombre para tu campaña (máximo 250 caracteres):\n\n    >>>")
    if len(nombre_campania) > 250:
            raise LargoExcedidoError()

    while True:
        fecha1 = input("Ingresa una fecha de inicio de campaña en formato 'DD, MM, AAAA': ")
        fecha2 = input("Ingresa una fecha de término de campaña en formato 'DD, MM, AAAA': ")

        try:      
            fecha_inicio = datetime.strptime(fecha1, "%d, %m, %Y").date()
            fecha_termino = datetime.strptime(fecha2, "%d, %m, %Y").date()

            break  
        except ValueError:
            input("Al menos una fecha es inválida, intenta de nuevo\n\nEnter para continuar...")
        
    creacion = True
    datos_anuncio = agregar_anuncio(creacion)
    print(datos_anuncio)

    campania = Campania(nombre_campania, fecha_inicio, fecha_termino, *datos_anuncio)

    return campania


## FINALMENTE DEFINO LA FUNCION MENU PRINCIPAL DONDE SE PUEDEN AGREGAR MAS ANUNCIOS, VISUALIZAR LOS DATOS DE LA CAMPAÑA,
#  MODIFICAR EL NOMBRE DE LA CAMPAÑA Y VISUALIZAR LOS FORMATOS Y SUBTIPOS SOPORTADOS DE LOS ANUNCIOS
def menu_principal(mi_campania):
    while True:

        print("""
    Que deseas hacer a continuacion?
            
1. Agregar mas anuncios
2. Visualizar datos de la campaña
3. Modificar nombre de campaña
4. Visualizar tipos y formatos de anuncios
5. Salir
    """)
        opcion = input("\n        >>> ")
        if opcion not in ["1","2","3","4","5"]:
            continue
        if opcion == "1":

            while True:
                new_anuncio = agregar_anuncio()
                if new_anuncio == "salir":
                    break
                else:
                    mi_campania.componer_anuncio(*new_anuncio)

        elif opcion == "2":
            print(mi_campania)
            input("\nEnter para continuar...")
        
        elif opcion == "3":
            nuevo_nombre = input("Ingrese el nuevo nombre (Máximo 250 caracteres)\n\n    >>>> ")
            mi_campania.nombre = nuevo_nombre

        elif opcion == "4":
            print(Anuncio.mostrar_formatos())
            input("\nEnter para continuar...")

        elif opcion == "5":
            exit()


## ESTABLECO EL OREDEN EN QUE SE LLAMAN A LAS FUNCIONES
mi_campania = crear_campana()
menu_principal(mi_campania)