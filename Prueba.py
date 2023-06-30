import os
import time
import numpy
import msvcrt
lista_rut=[]
lista_nombre_dueño=[]
lista_nombre_mascota=[]
lista_pisos=[]
lista_identificador_unico=[]
habitacion= numpy.zeros((5,2),int)
def mostrar_menu():
 while True:
      os.system('cls')
      print("""Menú Mascota Segura
     1.Grabar
     2.Buscar
     3.Retirarse
     4.salir""")
      
def validar_opcion():
        while True:
            try:
              opc = int(input("Ingrese opcion: "))
              if opc in(1,2,3,4):
                return opc
              else:
                 print("Opcion invalida")
            except:
             print("ERROR! debe ingresar un numero")
def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut: "))
            if rut >= 10000000 and rut <= 99999999:
                return rut
            else:
                print("ERROR rut entre 10000000 y 99999999")
        except:
            print("ERROR! debe ingresar un numero entero")


