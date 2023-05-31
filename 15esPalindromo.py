#! /usr/bin/env python
# -*- coding: utf-8 -*-
# ejemplo: radar, ala, somos, seres, ojo, reconocer, orejero, arenera, neuquen
# invertimos un string
def es_palindromo(cadena):
	invertida = ""
	for letra in cadena:
		invertida = letra + invertida
	if cadena == invertida:
		return True
	else:
		return False
cadena = input("Ingrese una palabra para probar si es palindromo: ")
if cadena.isalpha():
	pali = es_palindromo(cadena)
	if pali:
		print(cadena,"Es palindromo")
	else:
		print(cadena,"NO es palindromo")
else:
	print("Ingrese de nuevo")
#
"""
# otra opcion
def largo_cadena(cadena):
    cont = 0
    for i in cadena:
        cont += 1
    return cont
invertida = ""
cont = largo_cadena(cadena)
# print(cont)
indice = -1         # para tomar el último elemento de la cadena
while cont >= 1:
      invertida = invertida + cadena[indice]
      indice = indice + (-1)
      cont -= 1
# print(invertida)
# alreves = cadena[::-1]   # esto invierte el string
# print(alreves, "alreves")

if cadena == invertida:
	print(cadena,"Es palindromo")
else:
	print(cadena,"NO es palindromo")
"""
