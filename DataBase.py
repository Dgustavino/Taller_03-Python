import sqlite3
from sqlite3 import Error

def sqlite_create_database():

    try:
        conexion = sqlite3.connect
        return conexion

    except Error as error:
        print(error)


def table_operador(connection):

    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE Operador(nombre TEXT)")
        connection.commit()

    except Error:
        print(Error, 'Datos incorrectos')


def insert_operador(connection):
    
     try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO Operador(nombre) VALUES (?)")
        connection.commit()

     except Error:
        print(Error)


def table_SubEstaciones(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE SubEstacion(id INTEGER PRIMARY KEY, nombre TEXT)")
        connection.commit()

    except Error:
        print(Error, 'Datos incorrectos')

def insert_SubEstacion(connection):
    
     try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO SubEstacion(id, nombre) VALUES (?,?)")
        connection.commit()

     except Error:
        print(Error)

objeto_conexion = sqlite_create_database()
table_SubEstaciones(objeto_conexion)

Est_Oriente = (1, 'Cartago')
Est_Occidente = (2, 'Agua caliente')
Est_Guarco = (3, 'Tejar')

Estaciones_dict = {
           1: Est_Oriente,
           2: Est_Occidente,
           3: Est_Guarco
}

for key in Estaciones_dict:
    print(Estaciones_dict[key])
    insert_SubEstacion(objeto_conexion, Estaciones_dict[key])

def getEstaciones(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM SubEstacion")
        objeto_resultado = cursor.fetchall()
        connection.commit()

        return objeto_resultado

    except Error:
        print(Error)


resultado = getEstaciones(objeto_conexion)




