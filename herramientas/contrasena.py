'''Clase contrasena
Autor EmiliaT-M
En esta clase se encuentran los atributos que debe guardarse para una contraseña,
como usuario, sitio, contrasena'''

from datetime import datetime
from herramientas.cifraDatos import encrypt, decrypt

class Contrasena:
    
	#Metodo contructor del objeto
    def __init__(self, sitio, usuario, contrasena, fecha_creacion=None):
        self.__sitio = sitio
        self.__usuario = usuario
        self.__contrasena = contrasena  # Encriptar la contraseña
        self.__fecha_creacion = fecha_creacion if fecha_creacion else datetime.now()
        
		
	#Metodo que muestra informacion
    def mostrar_informacion(self):
        """Retorna la información de la contraseña en formato legible."""
        return (f"Sitio: {self.__sitio}\n"
                f"Usuario: {self.__usuario}\n"
                f"Contraseña: {self.__contrasena}\n"
                f"Fecha de creación: {self.__fecha_creacion}")

    # Metodos getter y setters de los atributos
    
    #Get sitio
    @property
    def sitio(self):
        return self.__sitio
    
	#Set sitio
    @sitio.setter
    def sitio(self, cambio):
        self.__sitio = cambio

	#Get usuario 
    @property
    def usuario(self):
        return self.__usuario
    
	#Set usuario
    @usuario.setter
    def usuario(self, cambio):
        self.__usuario = cambio

	#Get contrasena
    @property
    def contrasena(self):
        return self.__contrasena
    

	#Set contrasena
    @contrasena.setter
    def contrasena(self, cambio):
        self.__contrasena = encrypt(cambio)  # Encriptar la nueva contraseña

	#Get fecha_creacion
    @property
    def fecha_creacion(self):
        return self.__fecha_creacion

	#Set fecha de creacion
    @fecha_creacion.setter
    def fecha_creacion(self, cambio):
        self.__fecha_creacion = cambio