#!/usr/bin/env python
# -*- coding: utf-8 -*-
a = 'abra'
b = 'cad'
c = 'Nada'
d = 'Sip'
#print('{0}{1}{0}{3}{2}'.format("ABRA", b, c, d))
"""
Nombre = input("Ingresa tu nombre: ")
Edad = int(input("Bien, ahora ingresa tu edad \n"))
NombreMascota = input("Ingresa el nombre de tu mascota \n")
#print("Tu nombre es", Nombre, "y tienes", Edad, ". Tu mascota se llama:", NombreMascota)

#print("Tu nombre es {1} y tienes {0} años. Tu mascota se llama {2}".format(Edad,Nombre, NombreMascota))
"""
"""
#Para mostrar el texto con alineación a la derecha, izquierda o centrado pondríamos:
a = 'abra'
b = 'cad'
print('{0:<5}{1:^5}{0:>5}'.format(a, b))
"""
#print(' Video club '.center(50,"*"))  # centra el string dentro de 40 caracteres y rellena con *

print("Mi tabla de multiplicar:")
for indice in range(1,11):
	print('{0:<2}{1:^4}{2:^1}{3:>3}'.format("2 *", indice, "=", 2*indice,"|"))
     #print("2 *", indice, "=", 2*indice)
     #print ('{3}{0:2d}{3} {3}{1:3s}{3} {3}{2:4d}{3}'.format(indice, "->", indice * indice * indice, "|"))
