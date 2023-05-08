from clasePlan import *
import csv

class ManejaPlan:
    def __init__(self):
        self.__planes= []
    def agregarPlan(self,unPlan):
        self.__planes.append(unPlan)
    def archivero(self):
        archivo= open('Planes_ej5.csv')
        lector= csv.reader(archivo,delimiter=';')
        for elemento in lector:
            cod= int(elemento[0])
            modelo= elemento[1]
            version= elemento[2]
            importe= float(elemento[3])
            unPlan= PlanAhorro(cod,modelo,version,importe)
            self.agregarPlan(unPlan)
        archivo.close()
        return()
    def modificaValor(self):
        i = 0
        for i in range(len(self.__planes)):
            print(self.__planes[i])
            importe = float(input('Ingrese nuevo valor: '))
            self.__planes[i].actualizaValor(importe)
        return()
    def obtenerCuota(self,i):
        cuotas = self.__planes[i].getCuotas()
        valor = self.__planes[i].getValor()
        return ((valor/cuotas)+valor * 0.10)
    def mostrarPlanes(self,importe):
        i = 0
        for i in range(len(self.__planes)):
            if(importe > self.obtenerCuota(i)):
                print(self.__planes[i])
        return
    def obtenerCuotaLicita(self,i):
        cuota = self.obtenerCuota(i)
        cuotasLicitas = PlanAhorro.getCantCuotas()
        return (cuota * cuotasLicitas)
    def mostrarMontos(self):
        i = 0
        for i in range(len(self.__planes)):
            print("Vehiculo:", self.__planes[i].getModelo())
            print("Monto: $", self.obtenerCuotaLicita(i))
        return()
    def cambiarCuotas(self,codigo,cant):
        i = 0
        bandera= None
        while not bandera and i in range(len(self.__planes)):
            if(codigo == self.__planes[i].getCod()):
                self.__planes[i].modificaCantCuotas(cant)
                bandera= True
                print("Se modificaron las cuotas.")
            i+=1
        return()