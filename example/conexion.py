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
        inforServer = conexion.get_server_info()
        print('info del servidor:', inforServer)

except Error as ex:
    print('Error durante la conexion: ', ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print('la conexion ha finalizado...')