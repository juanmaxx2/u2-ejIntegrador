class Cama:
    __idCama=int
    __Habitacion=None
    __Estado=bool
    __ApellidoNombre=None
    __Diagnostico=None
    __FechaI=None
    __FechaA=None
    
    def __init__(self,idCama,Habitacion,Estado,ApellidoNombre,Diagnostico,FechaI,FechaA):
        if int(idCama)>0 and int(idCama)<31: 
            if not Estado:
                self.__idCama=idCama
                self.__Habitacion=Habitacion
                self.__Estado=Estado
                self.__ApellidoNombre=None
                self.__Diagnostico=Diagnostico
                self.__FechaI=FechaI
                self.__FechaA=FechaA
            else:
                self.__idCama=idCama
                self.__Habitacion=Habitacion
                self.__Estado=Estado
                self.__ApellidoNombre=ApellidoNombre
                self.__Diagnostico=Diagnostico
                self.__FechaI=FechaI
                self.__FechaA=FechaA
        
    def getIdCama(self):
        return self.__idCama
    
    def getHabitacion(self):
        return str(self.__Habitacion)
    
    def getEstado(self):
        return str(self.__Estado)
    
    def getNombre(self):
        return str(self.__ApellidoNombre)
    
    def getDiagnostico(self):
        return self.__Diagnostico
    
    def getFechaI(self):
        return self.__FechaI
    
    def getFechaA(self,fecha):
        x=self.__FechaA=fecha
        return x