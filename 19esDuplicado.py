#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Escribe una función llamada "elimina_duplicados" que elimine los elementos duplicados en una lista 
# y los devuelva en una nueva lista.
lista = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Marzo", "Agosto", "Marzo", "Sept", "Junio", "Oct", "Nov", "Dic", "Dic"]
print("Esta es la lista original: ", lista)
"""
def elimina_duplicados(lista):
	resultado = []
	duplicados = []
	for mes in lista:
		if mes in resultado:
			duplicados.append(mes)
		else:
			resultado.append(mes)
	print("Lista modificada: ", resultado)
	print("Nombre removidos: ", duplicados)
  
elimina_duplicados(lista)
"""
# otra opcion

def elimina_duplicadosB(lista):
	listaElim = []
	listaLimpia = []
	#listaLimpia.append(lista[0])
	cant = 0
	totLista = len(lista)
	while cant < totLista:
		if lista[cant] in listaLimpia:
			listaElim.append(lista[cant])
		else:
			listaLimpia.append(lista[cant])
		cant = cant + 1
	print("Lista de repetidos", listaElim)
	print("Lista original sin los repetidos", listaLimpia)
# parte principal de mi programa
elimina_duplicadosB(lista)
