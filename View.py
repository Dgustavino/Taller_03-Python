from Model import *

class OperadorView:

    def __init__(self):
        self.breakliner = "***********************************"

    def welcome(self):
        print(self.breakliner+'\n'+ f"Bienvenido al Sistema.!!! ")

    def ver_operador(self, operador):
        print(self.breakliner+'\n Hola Operador: '+ operador.nombre)

    def mensaje(self,mensj):
        print(mensj+'\n')

    def goodbye(self):
        print('\n'+self.breakliner+ "ADIOS" + self.breakliner)


class EstacionView:

    def ver_subestaciones(self, estacion):
        print('\n SubEstacion: '+ estacion.nombreEst)
