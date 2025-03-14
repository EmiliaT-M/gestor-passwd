'''Archivo que gestiona y valida los datos ingresador por el usuario
para manejar los posibles errores'''

#Importaciones
import re
from conexionSQL.conexionBD import ConexionBD
from herramientas.contrasena import Contrasena
from herramientas.cifraDatos import encrypt, decrypt

class GestorContrasena:
    
	#Metodo constructor del objeto
    def __init__(self, db_path):
        #Conexion a gestorDb.db
        self.conexion = ConexionBD(db_path) 
        self.conexion.conectar() 
        

	#Metodo de tipo estatico que valida los sitios sean validos
    @staticmethod
    def validar_url(url):
        """Valida si una URL es válida con una expresion regular"""
        regex = re.compile(
            r'^(https?:\/\/)'  # http:// o https://
            r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # Dominio
            r'(:[0-9]+)?'  # Puerto opcional
            r'(\/[^\s]*)?$'  # Ruta opcional
        )
        return re.match(regex, url) is not None

	#metodo que valida los campos y agrega datos a la BD
    def agregar_contrasena(self, usuario, contrasena, sitio):
        
        #validacion de cadenas
        cadena_errores = ""

        # Validación de datos
        if not contrasena:
            cadena_errores += "Contraseña está vacía.\n"
        if not usuario:
            cadena_errores += "Usuario está vacío.\n"
        if not sitio:
            cadena_errores += "Sitio está vacío.\n"
        if len(usuario) < 2:
            cadena_errores += "Nombre de usuario demasiado corto.\n"
        if not self.validar_url(sitio):
            cadena_errores += "URL inválida. No olvides ingresar http://www. o https://www...\n"

        # Si hay errores, retornar el mensaje de error
        if cadena_errores:
            return cadena_errores.strip()

        # Encriptar la contraseña
        contrasena_encriptada = encrypt(str(contrasena))
        
        # Crear un objeto Contrasena
        nueva_contrasena = Contrasena(sitio, usuario, contrasena)

        # Guardar en la base de datos
        self.conexion.agregar_contrasena(usuario, nueva_contrasena.contrasena, sitio, nueva_contrasena.fecha_creacion)
        return "Contraseña agregada correctamente."


	#Metodo que elimina datos teniendo como parametro el sitio
    def eliminar_datos(self, sitio):
        """Elimina una contraseña de la base de datos por sitio."""
        if not sitio:
            return "El sitio no puede estar vacío."
        self.conexion.eliminar_datos(sitio)
        return f"Contraseña para el sitio {sitio} eliminada correctamente."

	#--Metodo que muestra los datos del usuario recibido como parametro--
    def mostrar_contrasenas_usuario(self, usuario):
        """Muestra todas las contraseñas de un usuario."""
        if not usuario:
            return "El usuario no puede estar vacío."
        datos = self.conexion.obtener_datos_usuario(usuario)
        print(datos)
        if not datos:
            return "No se encontraron contraseñas para este usuario."
        resultado = ""
        for fila in datos:
            #Corregir
            sitio, usuario, contrasena_encriptada, fecha = fila
            contrasena_desencriptada = decrypt(contrasena_encriptada)
            resultado += (
                f"Sitio: {sitio}\n"
                f"Usuario: {usuario}\n"
                f"Contraseña: {contrasena_desencriptada}\n"
                f"Fecha de creación: {fecha}\n"
                "-" * 30 + "\n"
            )
        return resultado.strip()

	#Metodo que cirra la conexion entre la aplicacion y la Base de datos (BD)
    def cerrar_conexion(self):
        """Cierra la conexión a la base de datos."""
        self.conexion.desconectar()


