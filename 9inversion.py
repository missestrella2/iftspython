#!/usr/bin/env Python
# -*- coding: utf-8 -*-
# Escribir un programa que pregunte al usuario una cantidad a invertir, el interés 
# anual y el número de años, y muestre por pantalla el capital obtenido en la 
# inversión.
"""
def validoCantidad():
	valido = 0
	while valido == 0:
		try:
			cantImp = float(input("Ingrese importe a invertir: "))
		except ValueError:
			print("Debes escribir un número.")
		else:
			if cantImp <= 0:
				print("El valor debe ser mayor a Cero.")
			else:
				valido = 1
	return cantImp
valido = 1
while valido == 1:
	try:
		cantInt = int(input("Ingrese Interes Anual: "))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if cantInt <= 0:
			print("El valor debe ser mayor a Cero.")
		else:
			valido = 0
while valido == 0:
	try:
		cantAnios = float(input("Ingrese cantidad de Años: "))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if cantAnios <= 0:
			print("El valor debe ser mayor a Cero.")
		else:
			valido = 1
#-------- parte principal de mi programa --------------
cant = 0
while cant < cantAnios:
	interes = cantInt * cantImp / 100
	print(interes)
	cantImp = cantImp + interes
	cant += 1
print("Capital resultante: ",cantImp)
"""
#********************************************************************
#************ otra opcion usando funciones para hacer cada validacion
#********************************************************************
"""
def ingresar_y_validar_capital(): 
    input_OK = False   

    while not input_OK:
        try:
            input_valor = float(input("Ingresa la cantidad a invertir:" ))
        except ValueError:
            print(" <ERROR> Debes ingresar un número entero o decimal")                              
        else:
            if input_valor <= 0:
                print(" <ERROR> Debes ingresar un número entero o decimal mayor que 0 (cero)")                              
            else:
                input_OK = True

    return input_valor
##############################################
def ingresar_y_validar_tasa():    
    input_OK = False

    while not input_OK:
        try:
            input_valor = float(input("Ingresa la tasa de interes de  anual a invertir:" ))
        except ValueError:
            print(" <ERROR> Debes ingresar un número entero o decimal")                              
        else:
            if input_valor <= 0 :
                print(" <ERROR> Debes ingresar un número entero o decimal mayor que 0 (cero)")                              
            else:
                input_OK = True

    return round(input_valor/100,4)
##############################################
def ingresar_y_validar_pĺazo():   
    input_OK = False 

    while not input_OK:
        try:
            input_valor = int(input("Ingresa la cantidad a meses:" ))
        except ValueError:
            print(" <ERROR> Debes ingresar un número entero ")                              
        else:
            if input_valor <= 0:
                print(" <ERROR> Debes ingresar un número entero o decimal mayor que 0 (cero)")                              
            else:
                input_OK = True

    return round(input_valor/12,2)
#################### parte principal del programa ##########################
capital = ingresar_y_validar_capital()    
tasa_interes = ingresar_y_validar_tasa()    
plazo = ingresar_y_validar_pĺazo()    
resultado = 0
resultado = round(capital * plazo * tasa_interes,2)
print("El resultado de intereces obtenidos es de:", resultado)
"""
#************************************************************************
#**************** otra opcion re-utilizando codigo **********************
#************************************************************************
