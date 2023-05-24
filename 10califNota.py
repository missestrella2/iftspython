# Se pide obtener la calificación final de un examen, teniendo un nro de respuesta correctas que suman 4 puntos c/u, 
# un nro de respuestas incorrectas que restan 1 punto por c/u y un nro de respuestas en blanco.
while True:
	try:
		respOk = int(input("Ingrese cantidad de respuestas correctas:"))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if respOk < 0:
			print("El valor debe ser mayor a Cero.")
		else:
			break
while True:
	try:
		respMal = int(input("Ingrese cantidad de respuestas Incorrectas:"))
	except ValueError:
		print("Debes escribir un número.")
	else:
		if respMal < 0:
			print("El valor debe ser mayor a Cero.")
		else:
			break
#
calif = (respOk * 4) - respMal
print("La calificación final es:", calif)
