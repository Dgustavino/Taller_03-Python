from Controller import Operador
import Model
import View
from DataBase import query


if __name__=="__main__":   

    Database = DataBase.database()
    nombre = str(input("Ingrese su Nombre:"))
    Database.Insert(id,nombre)

    control = Controller.Operador()
    control.agregarEst()

    vista = View.EstacionView()
    vista.ver_subestaciones()


