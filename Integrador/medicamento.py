class Medicamento:
    __idCama=int
    __idMedicamento=int
    __Nombre=''
    __Monodroga=''
    __Presentacion=''
    __CantidadAplicada=''
    __PrecioTotal=''
    
    def __init__(self,idCama,idMedicamento,Nombre,Monodroga,Presentacion,CantidadAplicada,PrecioTotal):
        if int(idCama)>0 and int(idCama)<31: 
            if int(idMedicamento)>0 and int(idMedicamento)<101:
                self.__idCama=idCama
                self.__idMedicamento=idMedicamento
                self.__Nombre=Nombre
                self.__Monodroga=Monodroga
                self.__Presentacion=Presentacion
                self.__CantidadAplicada=CantidadAplicada
                self.__PrecioTotal=PrecioTotal
        
    def getIdCama(self):
        return self.__idCama
    
    def getIdmedicamento(self):
        return self.__idMedicamento
    
    def getNombre(self):
        return self.__Nombre
    
    def getMonodroga(self):
        return self.__Monodroga
    
    def getPresentacion(self):
        return self.__Presentacion
    
    def CantidadAplicada(self):
        return self.__CantidadAplicada
    
    def getPrecio(self):
        return self.__PrecioTotal