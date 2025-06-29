from datetime import datetime, date
from anuncio import Video, Display, Social 
from errores import LargoExcedidoError

class Campania:
    def __init__(self, nombre:str, fecha_inicio:date, fecha_termino:date, *datos_anuncio):
        self.__nombre = nombre
        self.__fecha_inicio = fecha_inicio
        self.__fecha_termino = fecha_termino
        self.__anuncios = [self.componer_anuncio(*datos_anuncio)]

## DEFINO EL METODO COMPONER_ANUNCIO EL CUAL RESPONDE DE MANERA DISTINTA EN BASE A SI SE ESTÁ CREANDO UNA INSTANCIA DE CAMPAÑA O SI LA
#  CAMPAÑA A FUE CREADA Y SOLO SE REQUIERE AÑADIR MAS ANUNCIOS, ESTO SE DEFINE CON EL PARAMETRO CREACION, EL CUAL PUEDE SER TRUE O FALSE
    def componer_anuncio(self,opcion,ancho, alto, url_archivo, url_clic, sub_tipo, duracion, creacion):
        if opcion == 1:
            new_anuncio = Video(url_archivo, url_clic, sub_tipo, duracion)
        elif opcion == 2:
            new_anuncio = Display(ancho, alto, url_archivo, url_clic, sub_tipo)
        elif opcion == 3:
            new_anuncio = Social(ancho, alto, url_archivo, url_clic, sub_tipo)
        if creacion:
            return new_anuncio
        else:
            self.__anuncios.append(new_anuncio)

    ##### GETTER Y SETER NOMBRE #####
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        if len(nombre) <= 250:
            self.__nombre = nombre

        else:
            raise LargoExcedidoError()

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
    
    ##### SOBRECARGA DE __STR__ #####

    def __str__(self):
        videos = 0
        displays = 0
        sociales = 0
        for  anuncio in self.anuncios:
            if isinstance(anuncio, Video):
                videos += 1
            if isinstance(anuncio, Display):
                displays += 1
            if isinstance(anuncio, Social):
                sociales += 1
            
        return f"""
Nombre de la campaña: {self.nombre}
Anuncios: {videos} Video, {displays} Display, {sociales} Social
"""



