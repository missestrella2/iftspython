#2)Utilizando un bucle “while”, elaborar un código
#que imprima en pantalla cada uno de los
#elementos de una lista y simultáneamente los
#elimine, hasta quedar vacía.

lista_de_prueba=[5,7,3]

while len(lista_de_prueba)>0:
    indice=len(lista_de_prueba)-1
    print(lista_de_prueba[indice])
    lista_de_prueba.pop(indice)


    

