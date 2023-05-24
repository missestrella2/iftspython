#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Se pide obtener que tipo de triángulo es. Sabiendo que ingresan 3 datos correspondientes al largo de cada 
# lado. Recordar: el triángulo equilátero tiene los 3 lados iguales, el isósceles 2 lados iguales y el escaleno 
# los 3 lados distintos.
# ------------------ validacion de datos ingresados -----------
"""
valido = 0
while valido == 0:
	try:
		ladoA = int(input("ingrece la medida del lado 1 en cm: "))
		ladoB = int(input("ingrece la medida del lado 2 en cm: "))
		ladoC = int(input("ingrece la medida del lado 3 en cm: "))
	except ValueError:
		print("La medida debe ser un munero mayor a 0")
	else:
		if ladoA <= 0:
			print("La medida 1 debe ser entero y mayor a 0.")
		elif ladoB <= 0:
			print("La medida 2 debe ser entero y mayor a 0.")
		elif ladoC <= 0:
			print("La medida 3 debe ser entero y mayor a 0.")
		else:
			valido = 1
"""
# -------------------- validaciones independientes -------------
"""
valido = 0
while valido == 0:
	try:
		ladoA = int(input("ingrece la medida del lado 1 en cm: "))
	except ValueError:
		print("La medida debe ser un munero mayor a 0")
	else:
		if ladoA <= 0:
			print("La medida 1 debe ser entero y mayor a 0.")
		else:
			valido = 1
while valido == 1:
	try:
		ladoB = int(input("ingrece la medida del lado 2 en cm: "))
	except ValueError:
		print("La medida debe ser un munero mayor a 0")
	else:
		if ladoB <= 0:
			print("La medida 2 no puede ser menor a 0.")
		else:
			valido = 0
while valido == 0:
	try:
		ladoC = int(input("ingrece la medida del lado 3 en cm: "))
	except ValueError:
		print("La medida debe ser un munero mayor a 0")
	else:
		if ladoC <= 0:
			print("La medida 3 no puede ser menor a 0.")
		else:
			valido = 1
"""
# ------ defino una funcion 
def validoIng(texto):
	valido = 0
	while valido == 0:
		try:
			lado = int(input(f"Ingrese la medida del {texto} en cm: "))
		except ValueError:
			print("La medida debe ser un valor numerico")
		else:
			if lado <= 0:
				print("La medida debe ser un entero mayor a 0.")
			else:
				valido = 1
	return lado
#-------------------- cuerpo principal --------------------

cantidad = 1
ladoA = validoIng("lado A")
ladoB = validoIng("lado B")
ladoC = validoIng("lado C")
"""
while cantidad <= 3:
	if ladoA == 0:
		ladoA = validoIng()
	elif ladoB == 0:
		ladoB = validoIng()
	else:
		ladoC = validoIng()
	cantidad += 1
"""
if ladoA == ladoB and ladoA == ladoC:
     print("El triagulo es un equilatero")
else:
	if ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
		print("El triangulo es un isósceles")
	else:
		print("el triangulo es un escaleno")
