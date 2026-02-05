from controladorATE import gestorAtencion
from controladorPAC import gestorPaciente
def encontrado(gestorP,gestorA):
    j=0
    print(f"Pacientes que no tuvieron atenciones: ")
    for i in range(gestorP.cantidad()):
        cant=gestorA.cantidadATE(gestorP.returnDNI(i))
        if cant==0:
            paciente=gestorP.returnNombre(i)
            print("PACIENTE: ",paciente)
            
def menu(xgp,xga):
    
    opcion=int(input("[1] para buscar las atenciones de una fecha y su importe\n[2] Para buscar pacientes y sus atenciones por su dni\n[3] para tener todos los pacientes que no tuvieron atenciones\n[4] Para mostrar la lista ordenada"))
    if opcion==1:
        unafecha=input("Ingrese la fecha: ")
        xga.buscarFecha(unafecha)
    elif opcion==2:
        unDNI=int(input("INGRESE DNI: "))
        if unDNI==xgp.buscarDNI(unDNI):
            cont=xga.cantidadATE(unDNI)
            print(" tiene",cont,"atenciones")
    elif opcion==3:
        encontrado(xgp,xga)
    elif opcion==4:
        xgp.ordenar()
        xgp.mostrar()
if __name__=='__main__':
    gestorAT=gestorAtencion()
    gestorPA=gestorPaciente()
    gestorAT.leerCSV()
    gestorPA.leerCSV()
    menu(gestorPA,gestorAT)
