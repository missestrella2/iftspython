valido = 0
while valido == 0:
	try:
		num = int(input("Ingrese numero:"))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if num < 0:
			print("El valor debe ser mayor a Cero.")
		else:
			valido = 1