#1) Ingresar precio y cantidad. Mostrar el total a pagar.
"""
precio=float(input("ingresa precio"))
cantidad=int(input("ingresa cantidad"))
suma=precio*cantidad
print(suma)
"""
#2) Ingresar 2 valores, sumarlos y mostrar el resultado, multiplicarlos y mostrar el resultado
"""
valor1=int(input("ingresa un n"))
valor2=int(input("ingresa otro n"))
suma=valor1+valor2
print(suma)
multiplico=valor1*valor2
print(multiplico)
"""
#3) Calcular el perímetro de un cuadrado
"""
lado=float(input("Te dire el perimetro de un cuadrado. Ingresa medida del lado"))
perimetro=lado*4
print(perimetro)
"""
#4) Ingresar 4 valores. Sumar los dos primeros, multiplicar los dos ultimos y mostrar los resultados.
"""
v1=float(input("ingresa un valor"))
v2=float(input("ingresa otro valor"))
v3=float(input("ingresa otro valor"))
v4=float(input("ingresa otro valor"))
suma=v1+v2
mult=v3*v4
print(suma)
print(mult)
"""
#5) Ingresan 4 valores, se pide el promedio y la suma. Mostrar ambos resultados
"""
v1=float(input("ingresa un valor"))
v2=float(input("ingresa otro valor"))
v3=float(input("ingresa otro valor"))
v4=float(input("ingresa otro valor"))
suma=v1+v2+v3+v4
promedio=suma/4
print(suma)
print(promedio)
"""
#6) Escriba el algoritmo para determinar la cantidad de minutos (y segundos)
# de acuerdo a una cantidad de segundo ingresados.

segundos=int(input("ingresa cantidad de seg"))

minutos = int(segundos/60)
segundos= segundos%60

print(minutos)
print(segundos)