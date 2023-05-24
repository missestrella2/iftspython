#!/usr/bin/env Python
# -*- coding: utf-8 -*-
#Escriba un programa que pida una distancia en pies o pulgadas y que escriba esa distancia en centímetros. 
# Se recuerda que un pie son doce pulgadas y una pulgada son 2,54 cm
#-------------------- validaciones de ingreso ------------------------
while True:
	try:
		ingOpcion = int(input("Ingrese 1 para Pies, 2 para Pulgadas: "))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if not(ingOpcion > 0 and ingOpcion < 3):
			print("Opción incorrecta.")
		else:
			break
#
while True:
	try:
		ingPies = float(input("Ingrese distancia: "))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if ingPies < 0:
			print("El valor debe ser mayor a Cero.")
		else:
			break
#---------------------------------------------------------------------
if ingOpcion == 1:
	resCent = float(ingPies) * 30.48
else:
	resCent = float(ingPies) * 2.54
print(ingPies," corresponde a ", resCent," centimetros.")
