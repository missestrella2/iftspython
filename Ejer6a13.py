#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 6) Escriba el algoritmo para determinar la cantidad de minutos 
#   (y segundos) de acuerdo a una cantidad de segundo ingresados.
"""
minutos = 0
segundos = 0
valor1 = int(input("Ingrese la cantidad de minutos a convertir: "))
minutos1 = valor1 / 60
print(round(minutos1,2))
minutos = valor1 // 60              # calcula el cociente usando //
segundos = valor1 - (minutos * 60)  # calculo el resto usando %
# segundos = valor1 % 60
print(valor1, "Equivale a", minutos, "minutos y", segundos, "segundos.")
print("Los segundos ingresados equivalen a %d minutos y %d segundos" %(minutos, segundos))
"""
# 7) Escriba un algoritmo que pida una distancia en pies y pulgadas y que escriba dicha distancia en centímetros. 
#  Se recuerda que:
#  1 PIE = 12 pulgadas 
#  1 pulgada = 2,54 cm
"""
resCent = 0
ingOpcion = int(input("Ingrese 1 para Pies, 2 para Pulgadas: "))
valor1 = float(input("Ingrese distancia: "))
if ingOpcion == 1:
	resCent = float(valor1) * 30.48  # convierte de Pies a centimetros
else:
	resCent = float(valor1) * 2.54   # convierte de Pulgadas a centimetros
print(ingPie"s," corresponde a ", resCent," centimetros.")
"""
# 8) Escriba un algoritmo que pida una temperatura en grados Celsius y que convierta dicha
# temperatura en grados Fahrenheit. Se recuerda que la relacion entre grados Celsius (C)
# y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32.
"""
gCelsius = float(input("Ingrese temperatura en Grados Celsius: "))
gFar = 1.8 * gCelsius + 32
print("Equivale en Fahrenheit a: ",gFar)
"""
# 9) Escriba un algoritmo que pregunte al usuario el número de horas trabajadas y el costo
#  por hora. Determinar el pago de jornal que le corresponde.

calcJornal = 0
numHoras = int(input("Ingrese cantidad de horas trabajadas por día: "))
pagoJornal = int(input("Ingrese el valor de la hora: "))
calcJornal = pagoJornal * numHoras
print("El valor del jornal es: ", calcJornal)

# 10) Calcular la distancia recorrida por un auto a velocidad constante y en un tiempo
#  determinado. Tener en cuenta la fórmula de Movimiento Rectilineo Uniforme:
#  Distancia = Velocidad * Tiempo 
# 11) Calcular el promedio de notas obtenidas por un alumno, teniendo 7 notas en el año.
# 12) Escribir un algoritmo que pregunte al usuario una cantidad a invertir, el interes anual,
#     y el numero de años. Mostrar el capital obtenido en la inversión.
# 13) Se pide determinar la calificación final de un examen, teniendo un nro de respuestas
#   correctas que suman 4 puntos c/u, un nro de respuestas incorrectas que restan 1 punto c/u
#   y un nro de respuestas en blanco.
