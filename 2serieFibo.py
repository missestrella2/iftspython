# serie Fibonacci
maxi = int(input("Ingrese el maximo: "))
serie = [0,1]  # 0 1 1 2 3 5 8...
uno = 0
dos = 1
suma = 0
while suma < maxi:
	suma = uno + dos
	if suma < maxi:
		serie.append(suma)
	uno = dos
	dos = suma
print(serie)
