import sqlite3
from sqlite3 import Error



class query:

    def __init__(self):
        self.db = "database.db"


    def sqlite_create_database(self):

        try:
            conexion = sqlite3.connect
            return conexion

        except Error as error:
            print(error)


    def table_operador(self,connection):

        try:
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE Operador(id PRIMARY KEY AUTOINCREMENT,nombre TEXT)")
            connection.commit()

        except Error:
            print(Error, 'Datos incorrectos')


    def Insert(self,id,nombre,connection):

            try:
                cursor = connection.cursor()
                query = ("INSERT INTO Operador(NULL,nombre) VALUES (?,?)")
                cursor.execute(query, [id,nombre])
                connection.commit()

            except Error:
                print(Error)


database = query()
database.sqlite_create_database()


