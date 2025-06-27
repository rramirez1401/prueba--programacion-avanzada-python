from datetime import date
from anuncio import Anuncio
from error import LargoExcedidoError

class Campania:
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.componer_anuncios()]


    def componer_anuncios(self, ):

        opcion = int(input("tipo anuncio?"))
        if opcion == 1:
            duracion = int(input("duracion?"))
        elif opcion == 2:

        

        self.anuncios.append



    ##### GETTER Y SETER NOMBRE #####
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) <= 250:
            self.__nombre = nombre

        else:
            raise LargoExcedidoError("El largo del texto supera los 250 caracteres")

    ##### GETTER Y SETER FECHA_INICIO #####   
    @property
    def fecha_inicio(self):
        return self.__fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, fecha_inicio):
        self.__fecha_inicio = fecha_inicio 

    ##### GETTER Y SETER FECHA_TERMINO #####
    @property
    def fecha_termino(self):
        return self.__fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, fecha_termino):
        self.__fecha_termino = fecha_termino  

    ##### GETTER ANUNCIOS #####
    @property
    def anuncios(self):
        return self.__anuncios


    def __str__(self):
        return f"""
Nombre de la campaña: {self.nombre}
"""
        pass

    def addAnuncio():
        pass

