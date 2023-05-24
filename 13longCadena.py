#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Definir una función que calcule la longitud de una lista o una cadena dada
def calcuLongitud(datoIngresado):
	cont = 0
	for cantidad in datoIngresado:
		cont = cont + 1
	print("La longitud de '", datoIngresado, "' es: ", cont)
	
# para calcular la longitud de una cadena ingresada (string)
print("Para calcular longitud de una cadena ingrese 0, de una lista 1")
opcion = int(input("Ingrese la opcion elegida: 0 para cadena, 1 para lista: "))
if opcion == 0:
	auxTexto = input("Ingrese un texto para calcular su longitud: ")
	calcuLongitud(auxTexto)               # usando la funcion creada por mi
	print("------ Ahora lo voy a resolver con la funcion len de python -----")
	longitud = len(auxTexto)              # usando la funcion de python
	print("La longitud del texto es: ", longitud)
else:
# para la lista:
    control = "s"
    newLista = []
    while control == "s" or control == "S":
        elemento = input("Ingrese elemento a la lista: ")
        newLista.append(elemento)
        control = input("Desea seguir ingresando? S(si), N(no): ").upper()
    calcuLongitud(newLista)               # usando la funcion creada por mi
    print("---- Ahora voy a resolverlo usando la funcion de len de python ----")
    longitud = len(newLista)              # usando la funcion creada por python
    print("La longitud de la lista es: ", longitud)
# longitud de una cadena dentro de una lista

# aqui comprobamos la cantidad de elementos de una lista y la cant.de caracteres de cada elemento
"""
mesLista = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Sept", "Oct", "Nov", "Dic"]
cont = 0
cont2 = 0
for cant in mesLista:
	cont2 = 0
	for cuento in cant:
		cont2 += 1
	print(cant,"tiene:", cont2,"caracteres.")
	cont = cont + 1
print("La lista tiene: ", cont, "items.")
"""
