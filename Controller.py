


class Operador:

     def __init__(self):
        
        self._lista_operador = [] 
        self.vista = OperadorView() 
        self.vista.welcome() 

    def addOperador(self,Operador): 
        
        self._lista_operador.append(Operador)


    def agregar(self): 
        
        try:
            datos_newStudent = input("Bienvenido al Sistema /n Ingrese su Nombre: ")
                
                operador_nuevo = Operador(datos_newOperador[0]) 
                self.addOperador(operador_nuevo)
                print("Hola" + operador_nuevo + "Nuevo...")
 
        except:
            self.vista.mensaje("Error en la entrada del usuario") 

class SubEstacion:

    def __init__(self):
        
        self._lista_subestacion = [] 
        self.vista = SubestacionView() 
        self.vista.welcome() 

    def addSubestacion(self,SubEstacion): 
        
        self._lista_subestacion.append(SubEstacion)


    def agregar(self): 
        
        try:
            datos_SubEstacion = input("Ingrese la subestacion que le corresponde: ")
                
                SubEstacion_nueva = SubEstacion(datos_SubEstacion[0]) 
                self.addSubestacion(SubEstacion_nueva)
                
        except:
            self.vista.mensaje("Error en la entrada del usuario") 


class Ciudad:

    def __init__(self):
        
        self._lista_ciudad = [] 
        self.vista = CiudadView() 
        self.vista.welcome() 

    def addCiudad(self,Ciudad): 
        
        self._lista_ciudad.append(Ciudad)


    def ListaCiudades(self): 

        self.vista.mensaje("LISTA DE CIUDADES: "+ str(len(self._lista_ciudad)) 

        if len(self._lista_ciudad)==0: 
            self.vista.mensaje("No se han ingresado datos aun!") 

        else: 
            for Ciudad in self._lista_ciudad: 
                self.vista.ver_ciudades(Ciudad) 
    