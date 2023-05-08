from clasePlan import *
from claseManejaP import *

if __name__ == '__main__':
    lista = ManejaPlan()
    lista.archivero()
    opcion= None
    while(opcion != '0'):
        opcion = input('''...Menu...
        0).Concluir
        1).Actualizar valor de vehiculos
        2).Mostrar planes con un importe 
        3).Monto licitado
        4).Modificar cuotas
            ''')
        if opcion== '1':
            lista.modificaValor()
        elif opcion == '2':
            importe = float(input('Ingresar importe: '))
            lista.mostrarPlanes(importe)
        elif opcion == '3':
            lista.mostrarMontos()
        elif opcion == '4':
            codigo = int(input('Ingresar el codigo del vehiculo: '))
            cant = int(input('Ingresar las cuotas minimas para licitar: '))
            lista.cambiarCuotas(codigo,cant)
