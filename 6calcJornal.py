#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escribir un programa que pregunte al usuario por el número de horas trabajadas y 
# el costo por hora. Después debe mostrar por pantalla el pago que le corresponde.
#
valido = True
while valido == True:
    try:
        numHoras = int(input("Ingrese cantidad de horas trabajadas por día: "))
        valido = False
    except ValueError:
        print("Debes escribir un número entero.")
while valido == False:
    try:
        pagoJornal = int(input("Ingrese el valor de la hora: "))
        valido = True
    except ValueError:
        print("Debes ingresar un valor numérico entero.")
calcJornal = pagoJornal * numHoras
print("El valor del jornal es: ", calcJornal)
