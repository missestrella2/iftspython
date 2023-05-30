#Asi seria sin capturar errores	

#num = int(input("Ingrese numero:"))

#Asi seria capturando errores
try:
		num = int(input("Ingrese numero:"))
		valido = 1
except ValueError:
		print("Debes escribir un número.")