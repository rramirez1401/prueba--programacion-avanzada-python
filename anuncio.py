
from abc import ABC, abstractmethod
from errores import *

class Anuncio(ABC):
    def __init__(self, ancho: int, alto:int, url_archivo:str, url_clic:str, sub_tipo:str):
        self.__ancho = ancho if ancho > 0 else 1
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_clic = url_clic
        self.__sub_tipo = sub_tipo
    
    ##### GETTER Y SETER ANCHO #####
    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho):
        if ancho > 0:
            self.__ancho = ancho
        else:
            self.__ancho = 1

    ##### GETTER Y SETER ALTO #####
    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, alto):
        if alto > 0:
            self.__alto = alto
        else:
            self.__alto = 1

    ##### GETTER Y SETER URL_CLICK #####
    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self, url_archivo):
        self.__url_archivo = url_archivo

    ##### GETTER Y SETER URL_CLICK #####
    @property
    def url_clic(self):
        return self.__url_clic
    
    @url_clic.setter
    def url_clic(self, url_clic):
        self.__url_clic = url_clic

    ##### GETTER Y SETER SUB_TIPO #####
    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @sub_tipo.setter
    def sub_tipo(self, sub_tipo):
        if (isinstance(self, Video) and sub_tipo in Video.sub_tipo
        or isinstance(self, Display) and sub_tipo in Display.sub_tipo
        or isinstance(self, Social) and sub_tipo in Social.sub_tipo):
            self.__sub_tipo = sub_tipo
        else:
            raise SubTipoInvalidoError()


    ##### MÉTODOS DE LA CLASE ANUNCIO #####
    @staticmethod
    def mostrar_formatos():
        print(f"""
FORMATO 1: {Video.FORMATO}
==================
- Subtipo 1: {Video.SUB_TIPOS}
- Subtipo 2: {Video.SUB_TIPOS}

FORMATO 2: {Display.FORMATO}
==================
- Subtipo 1: {Display.SUB_TIPOS}
- Subtipo 2: {Display.SUB_TIPOS}

FORMATO 3: {Social.FORMATO}
==================
- Subtipo 1: {Social.SUB_TIPOS}
- Subtipo 2: {Social.SUB_TIPOS}
""")
        pass

    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod    
    def redimensionar_anuncio():
        pass





class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        self.__ancho = 1
        self.__alto = 1
        self.duracion = duracion if duracion > 0 else 5
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.__sub_tipo = sub_tipo


    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self, duracion):
        self.__duracion = duracion

    def comprimir_anuncio():
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"{Video.FORMATO}  {self.duracion}"
        


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"{Display.FORMATO}"


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio():
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio():
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")

    def __repr__(self):
        return f"{Social.FORMATO}"

