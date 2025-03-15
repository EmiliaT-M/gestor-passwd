from herramientas.gestorContrasena import GestorContrasena

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- Gestor de Contraseñas ---")
    print("0. Ver contraseñas")
    print("1. Agregar contraseña")
    print("2. Mostrar contraseñas de un usuario")
    print("3. Eliminar contraseña")
    print("4. Actualizar contraseña")
    print("5. Guardar cambios y salir")
    print("6. Salir sin guardar cambios")


def main():
    db_path = "conexionSQL/gestorDB.db"
    gestor = GestorContrasena(db_path)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion=="0":
            gestor.mostrar_datos()

        elif opcion == "1":  # Agregar contraseña
            sitio = input("Ingrese el sitio (URL): ")
            usuario = input("Ingrese el usuario: ")
            contrasena = str(input("Ingrese la contraseña:"))
            resultado = gestor.agregar_contrasena(usuario, contrasena, sitio)
            print(resultado)

        elif opcion == "2":  # Mostrar contraseñas
            usuario = input("Ingrese el usuario: ")
            resultado = gestor.mostrar_contrasenas_usuario(usuario)
            print(resultado)

        elif opcion == "3":  # Eliminar contraseña
            sitio = input("Ingrese el sitio (URL) a eliminar: ")
            resultado = gestor.eliminar_datos(sitio)
            print(resultado)

        elif opcion == "4":  # Actualizar contraseña
            sitio = input("Ingrese el sitio (URL) a actualizar: ")
            nueva_contrasena = input("Ingrese la nueva contraseña: ")
            gestor.conexion.cambiar_contrasena(sitio, nueva_contrasena)
            print("Contraseña actualizada correctamente.")

        elif opcion == "5":  # Guardar y salir
            gestor.conexion.guardar_cambios()
            print("Cambios guardados. Saliendo...")
            break

        elif opcion == "6":  # Salir sin guardar 
            aux= input("Recuerda que no se guardan los cambios que hiciste.\n¿Deseas guardar cambios? si (s) /no (n)):")
            if aux.lower()=="s":
                gestor.conexion.guardar_cambios()
                print("Cambios guardados. Saliendo...")
                
            elif aux.lower()=="n":
                gestor.cerrar_conexion()
            
            else: 
                print("Saliendo sin guardar cambios...")
                gestor.cerrar_conexion() 
            break    
        else:
            print("Opción no válida. Intente nuevamente.")

    gestor.cerrar_conexion()

if __name__ == "__main__":
    main()