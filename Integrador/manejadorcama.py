from cama import Cama
from datetime import datetime
import numpy as np
import csv
class ManejadorCama:
    __Cantidad=0
    __Dimension=0
    __Incremento=5
    
    def __init__(self,Dimension=5,Incremento=5):
        self.__camas=np.empty(Dimension,dtype=Cama)
        self.__Cantidad=0
        self.__Dimension=Dimension

    def AgregarCama(self,cama):
        if self.__Cantidad==self.__Dimension:
            self.__Dimension+=self.__Incremento
            self.__camas.resize(self.__Dimension)
        self.__camas[self.__Cantidad]=cama
        self.__Cantidad+=1

    def Iniciar(self):
        archivo=open('camas.csv')
        reader=csv.reader(archivo,delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unaCama=Cama(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.AgregarCama(unaCama)
                
    def BuscarPaciente(self,paciente,ManejadorM):
        i=0
        while paciente!=self.__camas[i].getNombre():
            i+=1
        if paciente==self.__camas[i].getNombre():
            fecha=datetime.today().strftime('%d/%m/%Y')
            print('\nPaciente:{Nombre}                 Cama:{idcama}       Habitacion:{habitacion}'.format(Nombre=self.__camas[i].getNombre(),idcama=self.__camas[i].getIdCama(),habitacion=self.__camas[i].getHabitacion()))
            print('\nDiagnostico:{diagnostico}          fecha de Internacion:{Fecha}'.format(diagnostico=self.__camas[i].getDiagnostico(),Fecha=self.__camas[i].getFechaI()))
            print('\nFecha de Alta:', format(self.__camas[i].getFechaA(fecha)))
            print('\nMedicamento/Monodroga                 Presentacion       Cantidad       Precio')
            ManejadorM.getMed(self.__camas[i].getIdCama())
        else: print('\nNo existe el paciente')
    
    def BuscarDiagnostico(self,diagnostico):
        i=0
        while diagnostico!=self.__camas[i].getDiagnostico():
            i+=1
        if diagnostico==self.__camas[i].getDiagnostico():
            if self.__camas[i].getEstado:
                print('\nPaciente:{Nombre}                 Cama:{idcama}       Habitacion:{habitacion}'.format(Nombre=self.__camas[i].getNombre(),idcama=self.__camas[i].getIdCama(),habitacion=self.__camas[i].getHabitacion()))
                print('\nDiagnostico:{diagnostico}          fecha de Internacion:{Fecha}'.format(diagnostico=self.__camas[i].getDiagnostico(),Fecha=self.__camas[i].getFechaI()))
        else: print('\nNo se encontró el diagnostico')