'''Clase conexion base de datos.
Autor EmiliaT-M 
Contiene la conexion para la base de datos y los metodos que permitiran agregar, modificar o eliminar 
los datos contenidos de el gestorDB.db'''

import sqlite3

class ConexionBD:

    #Metodo constructor
    def __init__(self, db_path):
        self.db_path = db_path
        self.con = None
        self.cursor = None

    #Metodo que realiza la coneccion con la BD
    def conectar(self):
        """Establece la conexión a la base de datos."""
        self.con = sqlite3.connect(self.db_path)
        self.cursor = self.con.cursor()

    #Metodo que desconecta la conexion con la BD
    def desconectar(self):
        """Cierra la conexión a la base de datos."""
        if self.con:
            self.con.close()

    #Metodo que agrega datos de la contrasena a la BD
    def agregar_contrasena(self, usuario, contrasena, sitio, fecha):
        """Agrega una nueva contraseña a la base de datos."""
        self.cursor.execute(
            """INSERT INTO contrasenias (usuario, contrasena, fecha_creacion, sitio) 
            VALUES (?, ?, ?, ?)""", (usuario, contrasena, fecha, sitio)
        )
        

    #Metodo que elimina datos, teniendo el sitio como parametro
    def eliminar_datos(self, sitio):
        """Elimina una contraseña por sitio."""
        self.cursor.execute(
            "DELETE FROM contrasenias WHERE sitio=?", (sitio,)
        )
       

    #Metodo que realizar cambios de contraseña
    def cambiar_contrasena(self, sitio, contrasena):
        """Actualiza la contraseña de un sitio."""
        self.cursor.execute(
            "UPDATE contrasenias SET contrasena=? WHERE sitio=?", (contrasena, sitio)
        )
        

    #Metodo que cambia el nombre del usuario 
    def cambiar_usuario(self, sitio, usuario):
        """Actualiza el usuario de un sitio."""
        self.cursor.execute(
            "UPDATE contrasenias SET usuario=? WHERE sitio=?", (usuario, sitio)
        )
       

    #metodo que retorna los datos y recibe como parametro usuario
    def obtener_datos_usuario(self, usuario):
        """Obtiene todas las contraseñas de un usuario."""
        self.cursor.execute(
            "SELECT * FROM contrasenias WHERE usuario=?", (usuario,)
        )
        return self.cursor.fetchall()
    
    #Metodo que retorna los datos y recibe como parametro sitio
    def obtener_datos_sitio(self, sitio):
        """Obtiene los datos de un sitio específico."""
        self.cursor.execute(
            "SELECT * FROM contrasenias WHERE sitio=?", (sitio,)
        )
        return self.cursor.fetchall()

    #Metodo que guarda los datos agregados
    def guardar_cambios(self):
        """Guarda los cambios en la base de datos."""
        self.con.commit()