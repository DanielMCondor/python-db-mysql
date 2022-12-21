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
        cursor.execute('SELECT database();')
        registro = cursor.fetchone()
        print('Conectado a la BD: ', registro)
        cursor.execute('SELECT * FROM user')
        resultados = cursor.fetchall()
        for fila in resultados:
            print(fila[0], fila[1], fila[2])

        print('total de registros: ', cursor.rowcount)

except Error as ex:
    print('Error durante la conexion: ', ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print('la conexion ha finalizado...')