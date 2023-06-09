#!/usr/bin/env python
# -*- coding: utf-8 -*-
# De una lista de productos el operador introducirá el código del producto seleccionado, se mostrará el precio, 
# se le pedirá la cantidad y luego se mostrará el precio final de la factura.
def validoCodigo(codPermitido):
	valido = True
	while valido:
		try:
			codigo = float(input("Ingrese el Código: "))
		except ValueError:
			print("Ingrese un valor numérico")
		else:
			if codigo in codPermitido:
				valido = False
			else:
				print("Ingrese un codigo habilitado.")
	return codigo
def validoCantidad():
	valido = True
	while valido:
		try:
			cantidad = int(input("Ingrese cantidad de unidades: "))
		except ValueError:
			print("Ingrese un valor numérico entero.")
		else:
			if cantidad <= 0:
				print("Ingrese una cantidad mayor a 0.")
			else:
				valido = False
	return cantidad
def menu():
	print('''
	--------------------------------------
	     LISTA DE PRODUCTOS DISPONIBLES
	--------------------------------------
	PRODUCTO                        CODIGO
	--------------------------------------
	ALFAJOR ............................ 1.1
	CARAMELOS .......................... 2
	CHUPETIN ........................... 3
	GOMITAS ............................ 4
	CHOCOLATE .......................... 5
	JACK ............................... 6
	TOPOLINO ........................... 7
	PIRULIN ............................ 8
	AGUA ............................... 9
	GASEOSA ........................... 10
	''')
	# Se podría armar el menu dinámico....
	#nomProducto = ["ALFAJOR", "CARAMELOS","CHUPETIN","GOMITAS","CHOCOLATE","JACK","TOPOLINO","PIRULIN","AGUA","GASEOSA"]
	#cantProd = len(nomProducto)
	#for elementos in nomProducto:
	#	print(elementos,"......................... ",)
# --------- aqui comienza el bloque principal -------------
continua = "si"
total = 0
precioTotal = 0
while continua == "si":
	menu()
	relacion = {1.1:150, 2:20, 3:50, 4:80, 5:200, 6:150, 7:200, 8:100, 9:70, 10:120}
	codPermitido = relacion.keys()
	#
	codigo = validoCodigo(codPermitido)
	print("Su precio es: $", relacion[codigo])
	#
	cantidad = validoCantidad()
	precioTotal = float(relacion[codigo] * cantidad)
	print("El Subtotal a pagar es: $", precioTotal)
	
	total = total + precioTotal
	continua = input("Desea comprar otro producto?(si/no)").lower()
print("El total de su factura es: ", total)
