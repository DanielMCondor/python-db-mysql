def listar_usuarios(users):
    print("\nUsuarios: \n")
    contador = 1
    for user in users:
        datos = "{0} | User: {1} ({2})"
        print(datos.format(user[0], user[1], user[2]))
        contador += 1
    print(" ")

def pedir_datos_registro():
    usuario = input("Ingrese usuario: ")
    contrasenia = input("Ingrese contraseña: ")

    tupla = (usuario, contrasenia)
    return tupla

def pedir_datos_actulizacion(usuarios):
    listar_usuarios(usuarios)
    exite_id = False
    id_edit = input("Ingrese el id del usuario a editar: ")
    for user in usuarios:
        if str(user[0]) == id_edit:
            exite_id = True
            break

    if exite_id:
        usuario = input("Ingrese usuario a modificar: ")
        contrasenia = input("Ingrese contraseña a modificar: ")

        curso = (usuario, contrasenia, id_edit)
    else:
        curso = None

    return curso
        

def pedir_datos_eliminacion(usuarios):
    listar_usuarios(usuarios)
    existe_id = False
    id_eliminar = input("Ingrese el id (user) a eliminar: ")
    for  user in usuarios:
        if str(user[0]) == id_eliminar:
            existe_id = True
            break
    if not existe_id:
        id_eliminar = ""

    return id_eliminar
