#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# Escriba un programa que pida una temperatura en grados Celsius y que escriba esa 
# temperatura en grados Fahrenheit. Se recuerda que la relación entre grados 
# Celsius (C) y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32
#-------------------------------- validacion de ingreso -----------------------
valido = True
while valido == True:
	try:
		gCelsius = float(input("Ingrese temperatura en Grados Celsius: "))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if gCelsius < 0:
			print("El valor debe ser mayor a Cero.")
		else:
			valido = False
#-----------------------------------------------------------------------------
gFar = 1.8 * gCelsius + 32
print("Equivale en Fahrenheit a: ",gFar)
