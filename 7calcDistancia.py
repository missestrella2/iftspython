#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Calcular la Distancia recorrida por un auto a velocidad constante y en un tiempo 
# determinado. Tener en cuenta la fórmula de Movimiento Rectilíneo uniforme: 
# (Distancia es igual a Velocidad por Tiempo).
#
def calcularDistancia(velocidad, tiempo):
	distancia = 0
	distancia = velocidad * tiempo
	return distancia
# -------------- aqui comienza el programa ----------------------#	
valido = 1
while valido == 1:
    try:
        ingVelo = int(input("Ingrese la velocidad en Km/H: "))
    except ValueError:
        print("Debes escribir un número entero.")
    else:
        if ingVelo <= 0:
            print("Debe ingresar un numero mayor a 0.")
        else:
            valido = 0
#
while valido == 0:
    try:
        ingTiempo = float(input("Ingrese el tiempo expresado en Horas: "))
    except ValueError:
        print("Debes escribir un número.")
    else:
        if ingTiempo <= 0:
           print("Debe ingresar un numero mayor a 0")
        else:
           valido = 1
#
calDistancia = calcularDistancia(ingVelo, ingTiempo)
print("Recorrerá KM ", calDistancia," a ",ingVelo," en ", ingTiempo, "horas.")
