valido = 0
while valido == 0:
	try:
		num = int(input("Ingrese numero:"))
		valido = 1
	except ValueError:
		print("Debes escribir un número.")
		