#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1) Ingresar precio y cantidad. Mostrar el total a pagar.
"""
total = 0
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))
total = precio * cantidad
print("El total a pagar es: ", round(total,2))
"""
# 2) Ingresar 2 valores, sumarlos y mostrar el resultado, 
#    multiplicarlos y mostrar el resultado
"""
suma = 0
multi = 0
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
suma = valor1 + valor2
print("El resultado de la suma es: ", suma)
multi = valor1 * valor2
print("El resultado de la multiplicación es: ", multi)
"""
# 3) Calcular el perímetro de un cuadrado
"""
perimetro = 0
lado = int(input("Ingresar el valor de un lado del cuadrado: "))
perimetro = lado * 4
print("El perímetro del cuadrado es: ", perimetro)
"""
# 4) Ingresar 4 valores. Sumar los dos primeros, 
#    multiplicar los dos ultimos y mostrar los resultados.
"""
suma = 0
multi = 0
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercero valor: "))
valor4 = int(input("Ingrese el cuarto valor: "))
suma = valor1 + valor2
multi = valor3 * valor4
print("La suma de los dos primeros es: ", suma)
print("La multiplicación de los dos últimos es: ", multi)
"""
# 5) Ingresan 4 valores, se pide el promedio y la suma. 
#    Mostrar ambos resultados
promedio = 0
suma = 0
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))
valor3 = int(input("Ingrese el tercero valor: "))
valor4 = int(input("Ingrese el cuarto valor: "))
suma = valor1 + valor2 + valor3 + valor4
promedio = suma / 4
print("La suma de los valores es: ", suma)
print("El promedio de los valores es: ", promedio)
