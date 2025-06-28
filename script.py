from datetime import datetime
from campania import *



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
            datos_anuncio.append(input("\n\n        >>> "))

            if opcion == 1:
                datos_anuncio.append(int(input("Ingresa la duracion del video:\n\n        >>> ")))
            else:
                datos_anuncio.append(1)

            datos_anuncio.append(creacion)
            return datos_anuncio

        except ValueError:
            input("Entrada no válida, intenta de nuevo por favor\n\nEnter para continuar...")



def crear_campana():
    nombre_campania = input("Elige un nombre para tu campaña (máximo 250 caracteres):\n\n    >>>")
    if len(nombre_campania) > 10:
            raise LargoExcedidoError("El largo del texto supera los 250 caracteres")

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


def menu_principal(mi_campania):
    while True:

        print("""
    Que deseas hacer a continuacion?
            
1. Agregar mas anuncios
2. Visualizar datos de la campaña
3. Modificar nombre de campaña
4. Visualizar tipos y formatos de anuncios
5. 
    """)
        opcion = input("\n        >>> ")
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
            nuevo_nombre = input("Ingrese el nuevo nombre (Máximo 250 caracteres)")
            mi_campania.nombre = nuevo_nombre



mi_campania = crear_campana()
menu_principal(mi_campania)