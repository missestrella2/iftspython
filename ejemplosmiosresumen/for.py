#FOR lo que hace es recorrer los elementos 
#y sale del bucle cuando termino de recorrer
#La sintaxis básica es:
# for valor in lista_de_valores:
  # puedes usar la variable valor dentro de este bloque de codigo
#for, in -->> son palabras reservadas del bucle for
#se puede leer de la siguiente forma:
#por cada <valor> en la <lista_de_valores>


#Ejemplo 1 : recorrido de una lista que tiene adentro tuplas
lista_tuplas = [(1,2), (3,4)]

for a, b in lista_tuplas:
  print("a:", a, "b:", b)
  
"""
a,b -> valor iterador
lista_tuplas -> objeto a iterar
Salida
a: 1 b: 2
a: 3 b: 4
"""

#Ejemplo 2 : otro recorrido de una lista

A = ["hola", 1, 65, "gracias", [2, 3]]

for value in A:
    print(value)

#Ejemplo 3: recorrido de un diccionario
#Iterar sobre claves en un diccionario (también conocido como hashmap)

fruta_a_color = {"manzana": "#ff0000",
                 "lima": "#ffff00",
                 "naranja": "#ffa500"}

for key in fruta_a_color:
    print(key, fruta_a_color[key])

#asi imprimo solo las keys
for key in fruta_a_color:
    print(key)

#asi imprimo solo las values
for key in fruta_a_color:
    print(fruta_a_color[key])

#Ejemplo 4: otro recorrido de un diccionario
#usando .items
#me devuelve key y value

dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

for item in dict.items():
     print(item)

# Ejemplo 5: 
# Iterar sobre una lista y obtener el índice correspondiente con la 
# función enumerate() - enumerar
# la sintaxis seria for seguido de una variable que va a guardar el indice coma y el valor
# me devuelve indice seguido del elemento

A = ["esto", "es", "algo", "divertido"]

for indice,palabra in enumerate(A):
    print(indice, palabra)

