
lista=[1,2,2,5,5]
largolista=len(lista)

for elementos in lista:
    indice=0
    valido=0
    while indice<largolista:
        if lista[indice]==elementos:
            if valido!=0:
                print("esta duplicado")
            else:
                valido=1
        indice=indice+1
    
