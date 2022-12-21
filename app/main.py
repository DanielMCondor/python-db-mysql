from db.conexion import DAO
import funciones

def menuPrincipal():
    continuar = True
    while continuar:
        opcion_correcta = False
        while not opcion_correcta:
            print("=== MENÚ PRINCIPAL ===")
            print("1.- Listar usuarios")
            print("2.- Registrar usuario")
            print("3.- Actulizar usuario")
            print("4.- Eliminar usuario")
            print("5.- Salir")
            print("======================")
            opcion = int(input("Seleccione una opción: "))

            if opcion <1 or opcion>5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcion_correcta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:
        try:
            usuarios = dao.listar_usuarios()
            if len(usuarios) > 0:
                funciones.listar_usuarios(usuarios)
            else:
                print('No se encontraron usuarios...')
        except:
            print("Ocurrio un error...")
    elif opcion == 2:
        usuario = funciones.pedir_datos_registro()
        try:
            dao.registar_usuario(usuario)
        except:
            print("Ocurrio un error...")
    elif opcion == 3:
        try:
            usuarios = dao.listar_usuarios()
            if len(usuarios) > 0:
                usuario = funciones.pedir_datos_actulizacion(usuarios)
                if usuario:
                    dao.actulizar_usuario(usuario)
                else:
                    print('Id de usuario a actulizar no encontrado...\n')
            else:
                print('No se encontraron usuarios...')

        except:
            print("Ocurrio un error...")
    elif opcion == 4:
        try:
            usuarios = dao.listar_usuarios()
            if len(usuarios) > 0:
                id_eliminar = funciones.pedir_datos_eliminacion(usuarios)
                if not id_eliminar == "":
                    dao.eliminar_usuario(id_eliminar)
                else:
                    print("El id ingresado no es valido...\n")
            else:
                print('No se encontraron usuarios...')

        except:
            print("Ocurrio un error...")
    else:
        print("Opción no valida...")


menuPrincipal()