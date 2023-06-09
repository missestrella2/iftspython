#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ingresan dos palabras para saber si riman
# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que 
# decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
print("Vamos a ver si estas palabras riman.")
valido = True
while valido:
	try:
		uno = input("Dime la primera palabra: ")
	except ValueError:
		print("Ingrese un valor Alfabético.")
	else:
		if uno.isalpha():
			valido = False
while valido == False:
	try:
		dos = input("Dime la segunda palabra: ")
	except ValueError:
		print("Ingrese un valor Alfabético.")
	else:
		if dos.isalpha():
			valido = True
#
if len(uno) < 3 or len(dos) < 3:
	print("Las palabras tienen menos de 3 letras")
elif uno[-1] == dos[-1] and uno[-2] == dos[-2] and uno[-3] == dos[-3]:     # uno[-3:] == dos[-3:]:
	print(uno, "y", dos, "Riman")
elif uno[-1] == dos[-1] and uno[-2] == dos[-2]:                            # uno[-2:] == dos[-2:]:
	print(uno, "y", dos, "Riman un poco")
else:
	print(uno, "y", dos, "No riman")
''' [-3:-1] esto toma la ante-penultima y la penultima letra
if palabra1[-3:-1] == palabra2[-3:-1]:
    print(palabra1, "y", palabra2, "riman")
# [-2:-1] esto toma la penultima solamente
elif palabra1[-2:-1] == palabra2[-2:-1]:
    print(palabra1, "y", palabra2, "riman un poco")
else:
	print(palabra1, "y", palabra2, "no riman")
'''
