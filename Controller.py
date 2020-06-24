from Model import DatosOperador, DatosEstacion
from View import OperadorView, EstacionView
from os import system, name


class Operador:

    def __init__(self):
        
        self._lista_operador = []
        self.vista = OperadorView() 
        self.vista.welcome() 

    def addOperador(self,operador): 
        self._lista_operador.append(operador)

    def updateView(self): 
    
        if len(self._lista_operador)==0: 
            self.vista.mensaje("No se han ingresado datos aun!") 
        else:
            for operador in self._lista_operador: 
                self.vista.ver_operador(operador) 

    def stopProgram(self): 
        self.vista.goodbye() 
    

    def cleanTerminal(self):
        # for windows 
        if name == 'nt': 
            _ = system('cls') 
    
        # mac and linux
        else: 
            _ = system('clear') 


    def agregar(self): 
        
        try:
            Datos = input("Ingrese su Nombre: ").split()
            operador_nuevo = DatosOperador(Datos[0])
            self.addOperador(operador_nuevo)
 
        except:
            self.vista.mensaje("Error...") 

 

    def run(self):
        
        corriendo = True
        
        while corriendo == True:
            try: 
                self.agregar()
                self.updateView()
                #Aqui Metodos de Subestacion
                #Aqui Metodos de Ciudad
                userInput = input("Desea volver a utilizarlo? Y to continue /N to exit: ")

                if userInput =='Y':
                    self.cleanTerminal()
                else:
                    userInput =='N'
                    self.stopProgram()
                    corriendo = False
                    
            except:
                self.vista.mensaje("Error en la entrada del usuario...")


class SubEstacion:
    
    def __init__(self):
        self.lista_estacion = []
        self.View = EstacionView()

    def addEstacion(self,estacion): 
        self.lista_estacion.append(estacion)

    def updateView2(self):

        if len(self.lista_estacion)==0: 
            self.vista.mensaje("No se han ingresado datos aun!") 
        else:
            for estacion in self.lista_estacion:
                self.View.ver_subestaciones(estacion)

    def agregarEst(self): 
        
        try:
            Datos = input("Ingrese la Subestacion que le corresponde: ").split()
            estacion_nueva = DatosEstacion(Datos[0])
            self.addEstacion(estacion_nueva)
 
        except:
            self.vista.mensaje("Error...") 


if __name__=="__main__":    
    control= Operador()
    control.run()
    control2= SubEstacion()
    