#!/usr/bin/env python
# -*- coding: utf-8 -*-
# convertimos la primer letra de cada palabra en mayuscula - intentamos el método title()
# no usar El método capitalize() devuelve un string en el que solo la primera letra estará escrita en mayúsculas
# tampoco usar title() que pone en mayuscula la primer letra de cada palabra
"""
def titulo(cadena):
	print("llego a la funcion: ", cadena)
	nueva = ""
	inicioPalabra = True                #indica el inicio de una palabra
	for caracter in cadena:
		if caracter != " ":     # not caracter.isalpha():
			if inicioPalabra:
				nueva = nueva + caracter.upper() # convierte a mayuscula
				inicioPalabra = False  #ya no es el inicio de una palabra 
			else:
				nueva = nueva + caracter.lower() # convierte a minuscula
		else:
			nueva = nueva + caracter
			inicioPalabra = True
	return nueva
texto = input("Ingreso una oracion:")
nuevoTexto = titulo(texto)
print("retorno de la funcion: ", nuevoTexto)
"""
#OTRA OPCION
"""
texto = input("intrese texto: ")
largo= len(texto)
cont = 1 
letra = texto[0].upper()
nuevaFrase = letra
while(cont<largo):
	print(cont,texto[cont])
	if texto[cont-1] == " ":
		nuevaFrase =  nuevaFrase + texto[cont].upper()
	else:
		nuevaFrase =  nuevaFrase + texto[cont].lower()
	cont += 1
print(nuevaFrase)
"""
# otro ejemplo:
"""
texto = input("Ingrese texto: ").lower()
mayus = "si"
textoListo = ""
Letras = {
"a" : "A",
"b" : "B",
"c" : "C",
"d" : "D",
"e" : "E",
"f" : "F",
"g" : "G",
"h" : "H",
"i" : "I",
"j" : "J",
"k" : "K",
"l" : "L",
"m" : "M",
"n" : "N",
"ñ" : "Ñ",
"o" : "O",
"p" : "P",
"q" : "Q",
"r" : "R",
"s" : "S",
"t" : "T",
"u" : "U",
"v" : "V",
"w" : "W",
"x" : "X",
"y" : "Y",
"z" : "Z"}   # lo mismo para todas las letras
#
for letra in texto:
	print("indice:", letra)
	if mayus == "si" and not(letra == " "):
		letra = Letras[letra]
	if " " in letra:
		mayus = "si"
	else:
		mayus = "no"
	textoListo = textoListo + letra
print(textoListo)
"""
