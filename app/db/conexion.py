import mysql.connector
from mysql.connector import Error

class DAO():
    def __init__(self):
        try:
            self.conexion=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='123',
                db='dbprueba'
            )

        except Error as ex:
            print('Error durante la conexion: {0}'.format(ex))

    def listar_usuarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM user ORDER BY id ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print('Error durante la conexion: {0}'.format(ex))

    def registar_usuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO user (name, password) values('{0}', '{1}')"
                cursor.execute(sql.format(usuario[0], usuario[1]))
                self.conexion.commit()
                print("¡Usuario registrado!\n")
            except Error as ex:
                print('Error durante la conexion: {0}'.format(ex))

    def actulizar_usuario(self, usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE user SET name = '{0}', password='{1}' where id = {2}"
                cursor.execute(sql.format(usuario[0], usuario[1], int(usuario[2])))
                self.conexion.commit()
                print("¡Usuario actulizado!\n")
            except Error as ex:
                print('Error durante la conexion: {0}'.format(ex))

    def eliminar_usuario(self, id):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM user WHERE id = {0}"
                cursor.execute(sql.format(id))
                self.conexion.commit()
                print("¡Usuario eliminado!\n")
            except Error as ex:
                print('Error durante la conexion: {0}'.format(ex))
