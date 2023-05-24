#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# Calcular el promedio de nota obtenido por un alumno, teniendo 7 notas en el año.
nota = 0
promedio = 0
cant = 0
notaTotal = 0
#
def validoNota():
	valido = 0
	while valido == 0:
		try:
			notas = float(input("Ingrese nota a promediar: "))
		except ValueError:
			 print("Debe ingresar un valor numerico")
		else:
			if notas < 0 or notas > 10:
				print("La nota debe estar entre 0 y 10")
			else:
				valido = 1
	return notas
# ------------------- comienzo mi bloque principal ---------------
for cant in range(7):
	nota = validoNota()
	notaTotal = notaTotal + nota
#
promedio = notaTotal / 7
print("El promedio es: ", round(promedio,2))
# otra opcion usando un while dentro de otro while
# uno controla la cantidad de notas y el otro controla que el ingreso sea correcto
"""
nota = 0
promedio = 0
totalNota = 0
cant = 0
listaA = []
while cant < 7:
	while True:
		try:
			nota = float(input("Ingrese nota a promediar: "))
		except ValueError:
			 print("Debe ingresar un valor numerico")
		else:
			if nota < 0 or nota > 10:
				print("La nota debe estar entre 0 y 10")
			else:
				break
	listaA.append(nota)
	totalNota = totalNota + nota
	cant = cant + 1
#
cantidad = len(listaA)
promedio = totalNota / cantidad
print("El promedio es: ", round(promedio,2))
"""
