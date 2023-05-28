#1)Crear un bucle que almacene en una variable la
#suma de todos los elementos numéricos de una
#lista, con excepción del último.

#lista_bla = [1,1,1,5]
#contador=len(lista_bla)
#acumulador=0
''''
print("la lista tiene {} elementos".format(contador))

for indice,elementodelalista in enumerate(lista_bla):
    if indice < contador-1:
        acumulador=acumulador+elementodelalista
        print(acumulador)
'''

valores = [1,2,3,4,5]
espacios=len(valores)-1
i=0
acumulador=0

while i < espacios:
    acumulador = acumulador + valores[i]
    print(acumulador)
    i=i+1




