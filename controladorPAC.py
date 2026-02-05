from pacientes import paciente
from atenciones import atencion
import numpy as np
import csv
class gestorPaciente:
    __lista:list
    
    def __init__(self):
        self.__lista=[]
    def cantidad(self):
        return len(self.__lista)
    def agregarPaciente(self,xpac):
        self.__lista.append(xpac)
    def leerCSV(self):
        archivo=open('ej6/pacientes.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        
        for fila in reader:
            if bandera==True:
                bandera=False
            else:
                dni=int(fila[0])
                nomb=fila[1]
                unidad=fila[2]
                XP=paciente(dni,nomb,unidad)
                self.agregarPaciente(XP)
        archivo.close()
    def buscarDNI(self,xid):
        i=0
        
        while i<len(self.__lista) and xid != self.__lista[i].getDni():
            i+=1
        if i<len(self.__lista):
            print(self.__lista[i].getNombre(),end='')
        else:
            xid=0
        return xid
    
    def returnDNI(self,i):
        return self.__lista[i].getDni()
    def returnNombre(self,i):
        return self.__lista[i].getNombre()
    def ordenar(self):
        self.__lista.sort()
    def mostrar(self):
        for i in range(len(self.__lista)):
            print(self.__lista[i])
            