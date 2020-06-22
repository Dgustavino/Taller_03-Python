import sqlite3
from sqlite3 import Error

def sqlite_create_database():

    try:
        conexion = sqlite3.connect
        return conexion

    except Error as error:
        print(error)

cursor = connection.cursor()

def table_operador(connection):

    try:
        cursor.execute("CREATE TABLE Operador(nombre TEXT)")
        connection.commit()

    except Error:
        print(Error, 'Datos incorrectos')


def insert_operador(connection):
    
     try:
         cursor.execute("INSERT INTO Operador(nombre) VALUES (?)")
         connection.commit()

    except Error:
        print(Error)


objeto_conexion = sqlite_create_database()
table_operador(connection)





