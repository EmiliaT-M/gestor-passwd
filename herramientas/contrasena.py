from datetime import datetime
import cifraDatos 

'''Clase contrasena, contiene los atributos a guardar de las contrasenas, 
como sitio, usuario, contrasena fecha en la que fue agregada'''

class contrasena:

	#Metodo contructor de la clase
	def __init__(self, sitio, usuario, contrasena,fecha_creacion):
		self.__sitio=sitio
		self.__usuario=usuario
		self.__contrasena=cifraDatos.encrypt(contrasena)
		self.__fecha_creacion=datatime.now()

	#Metodo que retorna los valores  del objeto
	def mostrar_informacion():
		return "\tSitio: "+self.__sitio+"\tUsuario: "+self.__sitio+ "\tPassword: "+ self.__contrasena

	#Metodos get y set para atributos privados

	@property
	def sitio(self):
		return self.__sitio

	@sitio.setter
	def set_sitio(self, cambio):
		self.__sitio=cambio


	@property
	def usuario(self):
		return self.__usuario

	@usuario.setter
	def set_usuario(self, cambio):
		self.__usuario=cambio

	@property 
	def contrasena(self):
		return self.__contrasena
	@contrasena.setter
	def set_contrasena(self, cambio):
		self.__contrasena=cambio
	@property #Metodos set y get para fechas de creacion
	def fecha_creacion(self):
		return self.__fecha_creacion

	@fecha_creacion.setter
	def set_fecha_creacion(self,cambio):
		self.__fecha_creacion=cambio
