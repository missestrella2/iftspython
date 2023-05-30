#un contador es cuando necesitamos contar la cantidad de algo,
# por ejemplo la cantidad de veces de un bucle

######Ejemplos de contador

#contador de vueltas en un while

contador=0
while contador<5:
    contador=contador+1

print("el bucle WHILE dio {} vueltas".format(contador))

#contador de vueltas en un for

contador=0
for i in range(6):
    contador=contador+1
print("el bucle FOR dio {} vueltas".format(contador))

########Ejemplos de acumulador

#acumulador con while que en cada vuelta multiplica por 2
acumulador=1
contador=1
while contador<4:
    acumulador=acumulador*2
    contador=contador+1
print(acumulador)

#acumulador con for que en cada vuelta suma 5
acumulador=0
contador=1
for elementos in range(3):
    acumulador=acumulador+5
print(acumulador)



