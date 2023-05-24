Nombre = input("Ingresa tu nombre: ")
Edad = int(input("Bien, ahora ingresa tu edad \n"))
NombreMascota = input("Ingresa el nombre de tu mascota \n")
print("Tu nombre es", Nombre, "y tienes", Edad, ". Tu mascota se llama:", NombreMascota)

#en vez de usar concatenar, uso Format
#pongo llaves en donde quiero las variables y al final las pongo todas juntas con el format 
#si las dejo vacias las toma en el orden que esten
#sino les puedo poner el indice de posicion
print("Tu nombre es {1} y tienes {0} años. Tu mascota se llama {2}".format(Edad,Nombre, NombreMascota))

#con el format podemos formatear el texto, por ejemplo podemos alinearlo 
#poniendo algunos valores especiales dentro de las llaves
#Ejemplos:
#:> alinear a la derecha
#:>5 que la palabra ocupe 5 lugares y dentro de esos 5 lugares alinear hacia la derecha 

#Para mostrar el texto con alineación a la derecha, izquierda o centrado pondríamos:
a = 'ab'
b = 'ca'
print('{0:>15}{1:^5}{0:<25}'.format(a, b))


#Otro ejemplo
print("Mi tabla de multiplicar:")
for indice in range(1,11):
	print('{0:<2}{1:^4}{2:^1}{3:>3}'.format("2 *", indice, "=", 2*indice,"|"))
