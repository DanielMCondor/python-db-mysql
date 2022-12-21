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
        cursor.execute("UPDATE user SET name='Valentina' WHERE id=3")
        conexion.commit()
        print("Registro actualizado con éxito.")

except Error as ex:
    print('Error durante la conexion: ', ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print('la conexion ha finalizado...')