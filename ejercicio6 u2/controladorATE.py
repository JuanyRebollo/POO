from atenciones import atencion
import numpy as np
import csv
class gestorAtencion:
    __lista:np.ndarray
    __cant:int
    __cont:int
    def __init__(self,xcant=48):
        self.__cant=xcant
        self.__cont=0
        self.__lista=np.empty(self.__cant,dtype=atencion)
    def getCont(self):
        return self.__cont
    def agregarAtencion(self,xpac):
        
        self.__lista[self.__cont]=xpac
        self.__cont+=1
    def leerCSV(self):
        archivo=open('ej6/atenciones.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        
        for fila in reader:
            if bandera==True:
                bandera=False
            else:
                dni=int(fila[0])
                fecha=fila[1]
                importe=float(fila[2])
                XA=atencion(dni,fecha,importe)
                self.agregarAtencion(XA)
        archivo.close()
    
    def buscarFecha(self,xf):
        total=0
        i=0
        while i<self.__cant:
            if self.__lista[i].getFecha()==xf:
                total+=self.__lista[i].getImporte()
                print(self.__lista[i])
            i+=1
            
        if total>0:
            print("EL TOTAL PARA LA FECHA ",xf," ES ",total)
    def cantidadATE(self,dni):
        i=0
        c=0
        while i<self.__cant:
            if self.__lista[i].getDni()==dni:
                c+=1
            i+=1
        return c
    def returnDNI(self,i):
        return self.__lista[i].getDni()
