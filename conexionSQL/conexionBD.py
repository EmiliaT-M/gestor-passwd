#Conexion base de datos
import sqlite3

#Indicamos la conexion
con = sqlite3.connect("gestoBD.db")
#Agregamos el cursor
cursor=con.cursor()


#Metodo que agrega un elemento a la BD
def agregar_contrasena(usuario,contrasena, sitio):
    cursor.execute(
        """INSERT INTO contrasenia VALUES ('{usuario}','{contrasena}','{sitio}',{date})"""
    )
    con.commit()

#metodo que elimina fila
def eliminar_contrasena(usuario):
    cursor.execute(
       """DELETE FROM contrasenia WHERE usuario='{usuario}' """
    )
    con.commit()


#Metodo que cambia el valor de la contrasena
def cambiar_contrasena(sitio, contrasena):
    cursor.execute(
       """UPDATE FROM contrasenia SET contrasenia= '{contrasena}'WHERE sitio='{sitio}' """
    )
    con.commit()

def cambiar_usuario(usuario, sitio):
    cursor.execute(
       """UPDATE FROM contrasenia SET usuario= '{usuario}'WHERE sitio='{sitio}' """
    )
    con.commit()
    
                

