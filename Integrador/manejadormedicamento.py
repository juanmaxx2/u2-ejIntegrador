from medicamento import Medicamento
import csv
class ManejadorMedicamento:
    __lista=[]
    
    def __init__(self):
        self.__lista=[]
    
    def Iniciar(self):
        archivo=open('medicamentos.csv')
        reader=csv.reader(archivo, delimiter=';')
        bandera=True
        for fila in reader:
            if bandera:
                bandera=False
            else:
                unMedicamento=Medicamento(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6])
                self.__lista.append(unMedicamento)
        
    def getMed(self,idc):
        total=0
        for i in range(len(self.__lista)):
            if idc==self.__lista[i].getIdCama():
                print('{Medicamento}/{monodroga}                  {Presentacion}           {Cantidad}           {Precio}'.format(Medicamento=self.__lista[i].getNombre(),monodroga=self.__lista[i].getMonodroga(),Presentacion=self.__lista[i].getPresentacion(),Cantidad=self.__lista[i].CantidadAplicada(),Precio=self.__lista[i].getPrecio()))
                x=int(self.__lista[i].getPrecio())
                total+=x
        print('precio Adeudado                                                        {Precio}'.format(Precio=total))