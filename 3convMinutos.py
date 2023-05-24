#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.
while True:
	try:
		ingSegundos = float(input("Ingrese cantidad de segundos para convertir a minutos: "))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if ingSegundos < 0:
			print("El valor debe ser mayor a Cero.")
		else:
			break
def convertiraMinutos(ingSegundos):
	restSegundos = 0
	minutos = ingSegundos / 60
	print(round(minutos,2))
	minutos = ingSegundos // 60      # calcula el cociente usando //
	restSegundos = ingSegundos % 60  # calculo el resto usando %
	print(ingSegundos, "corresponde a", minutos, "minutos y", restSegundos, "segundos")
#----------------------------------------------------
# bloque principal de mi programa
#----------------------------------------------------
convertiraMinutos(ingSegundos)
