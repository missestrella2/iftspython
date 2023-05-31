#! /usr/bin/env python
# -*- coding: utf-8 -*-
# invertimos un string no usar [::-1]       ejemplo: txt = "Hello World" [::-1]
# the slice statement [::-1] means start at the end of the string and end at position 0, move with the step -1, 
# negative one, which means one step backwards
# significa comenzar desde el final del string y culminar al inicio, se mueve de a uno con -1
#
#cadena = input("Ingrese un texto para invertir su orden: ")
"""
nuevaCadena = ""
for letra in cadena:
	#print(letra, nuevaCadena)
	nuevaCadena = letra + nuevaCadena
print(nuevaCadena)
"""
# otra manera ---------------------------------------------------
"""
indice = 0
nuevaCadena = ""     
largo = len(cadena)-1
for letra in range(largo,-1,-1):
	#print(cadena[letra],nuevaCadena)
	nuevaCadena = nuevaCadena + (cadena[letra])
print(nuevaCadena)
"""
# otra opcion usando una funcion que hace lo mismo que len() ----
"""
def largo_cadena(cadena):
    cont = 0
    for ind in cadena:
        cont += 1
    return cont
#
invertida = ""
cont = largo_cadena(cadena)
print(cont)
indice = -1         # para tomar el último elemento de la cadena
while cont >= 1:
	#print(cadena[indice], invertida)
	invertida = invertida + cadena[indice]
	indice = indice + (- 1)
	cont = cont - 1
print(invertida)
"""
