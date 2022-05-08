from manejadorcama import ManejadorCama
from manejadormedicamento import ManejadorMedicamento
if __name__=='__main__':
    ManejadorC=ManejadorCama()
    ManejadorM=ManejadorMedicamento()
    ManejadorC.Iniciar()
    ManejadorM.Iniciar()
    opcion=None
    while opcion!='3':
        print('\n')
        print('---0---0---0---0---0---0---0---0---0---0---0---0---0---0---0---')
        print('1) Dar de alta un paciente')
        print('2) Buscar un diagnostico')
        print('3) salir')
        opcion=input('ingresar la opcion que desea realizar:')
           
        if opcion=='1':
            paciente=input('\nIngrese el nombre de un paciente que desee buscar (el formato Apellido, Nombre):')
            ManejadorC.BuscarPaciente(paciente,ManejadorM)

        elif opcion=='2':
            diagnostico=input('\nIngrese el Diagnostico a buscar:')
            ManejadorC.BuscarDiagnostico(diagnostico)
    
    