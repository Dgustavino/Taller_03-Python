from Model import DatosOperador, DatosEstacion
from View import OperadorView, EstacionView
from os import system, name
import DataBase
import csv


class Operador:

    #pedir nombre
    #mostrar id y nombre
    def __init__(self):

        self.View = OperadorView()
        self.lista_estacion = []
        self.View = EstacionView()

    #pedir nombre subestacion
    def addEstacion(self,estacion): 
        self.lista_estacion.append(estacion)

    
    def updateView(self):

        if len(self.lista_estacion)==0: 
            self.vista.mensaje("No se han ingresado datos aun!") 
        else:
            for estacion in self.lista_estacion:
                self.View.ver_subestaciones(estacion)

    def agregarEst(self): 
        
        try:
            Datos = input("Ingrese la Subestacion: ").split()
            estacion_nueva = DatosEstacion(Datos[0])
            self.addEstacion(estacion_nueva)
 
        except:
            self.vista.mensaje("Error...") 


class SubEstacion:
    
     """Cartago"""
    #leerArchivo(csv.)
    def leerArchivo(self):
        
        with open('mediciones.csv') as f:
            reader = csv.reader(f, delimeter=",")
            for row in reader:
                print("Hora: {0}, Id_ciudad: {1}, KWatss: {2}".format(row[0], row[1], row[2]))


    #generarCuidades()->Occidental,Oriental,Guarco.
    def generarCuidades(self):

        self.lista_ciudades = [[1,'Occidental', 2,'Oriental', 3,'Guarco']]
        

    #separarDatos()
    


class Ciudad:
    #AdjuntarConsumo()
    #calcular_HoraPico()
    #consumo_total()

control = Controller.SubEstacion()
control.leerArchivo()


   
    