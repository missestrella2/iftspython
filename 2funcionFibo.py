#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# Esto es un ejemplo de uso de Funcion con paso de parámetros y validacion de ingreso
# valido que el ingreso sea numérico y que sea mayor a 0
valido = 0
while valido == 0:
	try:
		num = int(input("Ingrese limite para la serie Fibonacci:"))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if num < 0:
			print("El valor debe ser mayor a Cero.")
		else:
			valido = 1
# aqui definimos la funcion que va a tomar el numLimite ingreso originalmente en num
def fibo(numLimite=10):
	serie = [0,1]   # 0 1 1 2 3 5 
	uno = 0
	dos = 1
	tres = 0
	otro = "01"
	while tres < numLimite:
		tres = uno + dos
		if tres < numLimite:
			serie.append(tres)       # la serie en formato lista
			otro = otro + str(tres)  # la serie en formato string
			uno = dos
			dos = tres
	print(serie)
	return otro  # serie lo muestra en formato lista
# Ahora hacemos la llamada a la funcion pasando el parámetro de limite ingresado en num
#fibo(num)                           # llamada a funcion cuando no tiene return
serieFibo = fibo(num)                # guardamos el valor que retorna la funcion en serieFibo
print(serieFibo)                     # muestro la variable serieFibo que tiene el resultado de la funcion
