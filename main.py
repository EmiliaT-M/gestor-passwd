
def menu():
    while True:
        print("\n--- Gestor de Contraseñas ---")
        print("1. Agregar contraseña")
        print("2. Ver contraseñas")
        print("3. Buscar contraseña")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            servicio = input("Nombre del servicio: ")
            usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            agregar_contraseña(servicio, usuario, contraseña)
            print("¡Contraseña guardada exitosamente!")
        elif opcion == "2":
            ver_contraseñas()
        elif opcion == "3":
            servicio = input("Nombre del servicio a buscar: ")
            buscar_contraseña(servicio)
        elif opcion == "4":
            print("¡Adiós!")
            break
        else:
            print("Opción inválida. Inténtalo nuevamente.")

class main:
	menu()
