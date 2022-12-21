import mysql.connector
from mysql.connector import Error

try:
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123',
        db='dbprueba'
    )

    if conexion.is_connected():
        print('conexion exitosa...')
        cursor = conexion.cursor()
        nombre = input('Ingrese user: ')
        contrasenia = input('Ingrese password: ')
        # cursor.execute('INSERT INTO user (name, password) values ("renato", 147)')
        sentencia = "INSERT INTO user (name, password) values ('{0}', {1})".format(nombre, contrasenia)
        cursor.execute(sentencia)
        conexion.commit()
        print("Registro insertado con éxito.")

except Error as ex:
    print('Error durante la conexion: ', ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print('la conexion ha finalizado...')