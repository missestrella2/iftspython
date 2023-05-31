cadena = "Hola, que tal. que te pasa"

####encontrar el indice de un caracter de una cadena

#Esto recorre "cadena" imprimiendo los caracteres
"""
cadena = "Hola, que tal. que te pasa"
for caracteres in cadena: 
    print(caracteres)
"""
#asi se obtiene una letra de un string segun su indice
"""
oracion="Esto es una oracion larga"
print(oracion[2]) #esto devuelve la letra "t" (recordar que empieza a contar de 0)
print(oracion[-1]) #esto devuelve la ultima letra "a"
print(oracion[-2]) #esto devuelve la anteultima letra "g"
print(oracion[:-1]) #esto devuelve TODA la oracion MENOS la ultima letra
print(oracion[:-3]) #esto devuelve TODA la oracion MENOS las 3 ultimas letras
print(oracion[-4:-1]) #esto devuelve DESDE la letra 4 contando desde el final hasta la ultima letra sin incluirla
print(oracion[-4:]) #esto devuelve DESDE la letra 4 contando desde el final hasta la ultima letra
"""

#asi se imprime el indice de cada letra de un string con un for
"""
indice=0
for letras in oracion:
    print(indice) 
    indice=indice+1
"""
#Esto recorre "cadena" imprimiendo los caracteres y los indices
"""indiceultimaletra=len(cadena)
indice=0
for caracteres in range(indiceultimaletra):
    print("Letra: {}. Indice: {}.".format(cadena[indice],indice))
    indice=indice+1
"""

#Esto recorre "cadena" encontrando los espacios en blanco
"""
indiceultimaletra=len(cadena)
indice=0
for caracteres in range(indiceultimaletra):
    if cadena[indice]==" ":
        print("espacio encontrado")
    indice=indice+1

"""





