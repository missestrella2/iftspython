#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escriba una función es_bisiesto() que determine si un año es un año bisiesto. 
# Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400.
"""
def es_bisiesto(anio):
	if anio % 4 == 0 and (not(anio % 100 == 0)):
		resultado = "El año " + str(anio) + " es un año bisiesto porque es multiplo de 4"
	elif anio % 400 == 0:
		resultado = "El año " + str(anio) + " es un año bisiesto porque es multiplo de 400"
	else:
		resultado = "El año " + str(anio) + " no es bisiesto"
	return resultado
#------ aqui empieza mi programa -----------
print("Comprueba años bisiestos")
valido = True
while valido:
  try:
	  anio = int(input("Escriba un año y le dire si es bisiesto: "))
  except ValueError:
	  print("ingrese un valor numérico")
  else:
	  if año <= 0:
		  print("Ingrese un año mayor a cero.")
	  else:
		  valido = False
#
print(es_bisiesto(anio))
"""
#otro 
"""
valido = True
while valido:
  try:
	  año = int(input("ingresar un año: "))
  except ValueError:
	  print("ingrese un valor numérico")
  else:
	  if año <= 0:
		  print("Ingrese un año mayor a cero.")
	  else:
		  valido = False

def es_bisiesto(año):
	if ((año % 4 == 0) and (año % 100 != 0)) or (año % 400 == 0):
		print("El año",año,"es bisiesto")
	else:
		print("El año",año,"no es bisiesto")
#
es_bisiesto(año)
"""
