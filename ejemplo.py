#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#1)Ingresar precio y cantidad, mostrar el total a pagar.
"""
precio = int(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))
importe = precio * cantidad
print("El resultado de precio ", precio, " por cantidad ", cantidad, " es: ", importe)
print("El resultado es: " + str(importe))
"""
#2)Ingresar 2 valores numéricos enteros. Sumarlos y mostrar el resultado. Multiplicarlos y mostrar el resultado:
"""
num1=int(input("Ingrese el primer valor:"))
num2=int(input("Ingrese el segundo valor:"))
suma=num1+num2
producto=num1*num2
print("La suma de los valores es ", suma)
print("El producto de los valores es ", producto)
#4)Ingresar 4 valores, sumar los dos primeros, 
# multiplicar los dos últimos. Mostrar resultados.
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercero valor: "))
num4 = int(input("Ingrese el cuarto valor: "))
suma = num1 + num2
producto = num3 * num4
print("La suma de los 2 primeros valores es: ", suma)
print("El producto del tercer y cuarto valor es: ", producto)
#5)Ingresados 4 valores, sacar el promedio. 
# Mostrar resultado de la suma y el promedio.
num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))
num3 = int(input("Ingrese el tercero valor: "))
num4 = int(input("Ingrese el cuarto valor: "))
suma = num1 + num2 + num3 + num4
promedio = suma / 4
print("La suma de los valores es: ", suma)
print("El promedio es: ", promedio)
"""
#1)Mostrar el incremento de cant desde 1 a 100 utilizando while y otra usando for.
"""
cant = 1
while cant <= 100:
    print(cant)
    cant = cant + 1
print("Ahora comienza For:")
for cant in range(1,101):
    print(cant)
"""
#2)Dadas 10 notas ingresadas, informar cuántos aprobaron (se aprueba con 4).
"""
def validoNota():
	ok = 0
	while ok == 0:
		try:
			notas = int(input("Ingrese la nota: "))
		except ValueError:
			print("Debe ingresar un numero entero mayor a 0 y menor a 11.")
		else:
			if notas <= 0 or notas > 10:
				print("La nota de ser mayor a 0 y menor a 11.")
			else:
				ok = 1
	return notas
#--------- aqui comienza mi programa ----------------
total = 0
for cantidad in range(1,11):
	nota = validoNota()
	if nota >= 4 and nota <= 10:
		total = total + 1
print("Han aprobado (for): ",total)
# o podemos utilizar un while dentro de otro while
"""
"""
cantidad = 0
total = 0
while cantidad < 10:
	ok = 0
	while ok == 0:
		try:
			nota = int(input("Ingrese la nota: "))
		except ValueError:
			print("Debe ingresar un numero entero mayor a 0 y menor a 11.")
		else:
			if nota <= 0 or nota > 10:
				print("La nota de ser mayor a 0 y menor a 11.")
			else:
				ok = 1
	if nota >= 4:
		total = total + 1
	cantidad = cantidad + 1
#
print("Han aprobado(while): ",total)
"""
#3) Ingresar una cantidad de personas, por cada una: ingresar la estatura 
#y mostrar el promedio de altura final.
"""
def validoCantPersona():
	cant = 0
	while cant == 0:
		try:
			personas = int(input("Cuantas personas hay:"))
		except ValueError:
			print("Ingrese un numero entero.")
		else:
			if personas <= 0:
				print("Ingrese un numero mayor a cero.")
			else:
				cant = 1
	return personas
def validoAltura():
	cant = 0
	while cant == 0:
		try:
			altura = float(input("Ingrese la altura: "))
		except ValueError:
			print("Puede Ingresar un numero decimal.")
		else:
			if altura <= 0:
				print("Debe ingresar un valor mayor a cero.")
			else:
				cant = 1
	return altura
#----------- aqui comienza mi programa -----------------
persona = validoCantPersona()
cant = 1
suma = 0
while cant <= persona:
    altura = validoAltura()
    suma = suma + altura
    cant = cant + 1
promedio = suma / persona
print("El promedio es ", round(promedio,2))
"""
#4)Ingresar cant de empleados de una empresa. Determinar cuántos ganan mas
# de 5000 (la hora), cuántos menos y el costo de la empresa en sueldos.
"""
def validoCantEmpleados():
	ok = 0
	while ok == 0:
		try:
			cantEmpleados = int(input("Cuantos empleados tiene la empresa: "))
		except ValueError:
			print("Ingrese un valor numérico.")
		else:
			if cantEmpleados <= 0:
				print("Debe ingresar un valor mayor a 0.")
			else:
				ok = 1
	return cantEmpleados
def validoSueldo(cant):
	ok = 0
	while ok == 0:
		try:
			ingSueldo = float(input(f"Ingrese el valor de la hora del empleado Nro. {cant}: "))
		except ValueError:
			print("Ingrese un valor numérico.")
		else:
			if ingSueldo <= 0:
				print("Debe ingresar un valor mayor a cero.")
			else:
				ok = 1
	return ingSueldo
# ---------- aqui comienza la parte principal de mi programa ----------
cant_empleados = validoCantEmpleados()
cant = 1
menor = 0
mayor = 0
costo = 0
while cant <= cant_empleados:
    sueldo = validoSueldo(cant)
    if sueldo < 5000:
        menor = menor + 1
    else:
        mayor = mayor + 1
    costo = costo + (sueldo * 8)
    cant = cant + 1
print("Cantidad de empleados con sueldos menor a 5000 es: ", menor)
print("Cantidad de empleados con sueldos mayor a 5000 es: ", mayor)
print("Gasto total de la empresa en sueldos por día es: ", costo)
"""
#5)Ingresado un nro, mostrar su tabla de multiplicación.
"""
def validoTabla():
	ingreso = 0
	while ingreso == 0:
		try:
			numero = int(input("Ingrese un numero: "))
		except ValueError:
			print("Ingrese un valor numérico.")
		else:
			if numero <= 0:
				print("Debe ingresar un valor mayor a cero.")
			else:
				ingreso = 1
	return numero
#------------ parte principal de mi programa ------------

num = validoTabla()
print("La Tabla del",num,":")
for cont in range(1,11):
    resultado = num * cont
    print(num,"*",cont,"=",resultado)
"""
# otra opcion sencilla usando una funcion Lambda ----
# Lambda: son funciones anónimas que solo pueden contener una expresión.
"""
numero = int(input("ingrese un numero: "))
print(f"Los resultados de la tabla del {numero}:")
print([numero * indice for indice in range(11)])
"""
#6)Ingresar una frase y determinar la cantidad de espacios que contiene.
"""
frase = input("Ingrese una frase:")
total = 0
cant = 0
while cant < len(frase):
	print(frase[cant], cant)
	if frase[cant] == " ":
		total = total + 1
	cant = cant + 1
print("La cantidad de espacios en blanco ingresados es de ",total)
"""
# otra opcion
"""
frase = input("ingresa una frase: ")
contador = 0

for indice in frase:
	print(indice)
	if indice == " ":
		contador=contador+1
#
print("La cantidad de espacios que contiene es: ", contador)
"""
