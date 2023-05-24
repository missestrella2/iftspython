# Accciones en una lista: agregar al final, eliminar, insertar
provinList = ["Buenos Aires", "La Pampa", "Rio Negro", "Corrientes", "Entre Rios","Mendoza", "Misiones"]
provinElim = []
provinNueva = list()
#print(provinList)
provinList.append("Tucuman")   # agrego un elemento a mi lista
print(provinList)
"""
del provinList[2]              # elimino el elemnto que este en la posición 2
print(provinList)
provinList.insert(2,"Rio Negro")
print(provinList)
del provinList[-1]             # eliminamos un elemnto desde el final de la lista
print(provinList)
provinList.append("Tucuman")   # agregamos un elemento al final
print(provinList)
print(sorted(provinList))      # ordena temporalmente la lista
print(provinList)
print(sorted(provinList, reverse=True))  # ordena de forma descendente de forma temporal
provinList.sort()              # ordena de forma definitiva la lista
print(provinList)
provinList.sort(reverse=True)  # ordena de forma inversa
print(provinList)
print(len(provinList))         # nos dice la cantidad de elemento de la lista
elimProv = provinList.pop(2)  # guarda el elemento borrado en una variable
print(provinList)
print(elimProv)
indice = provinList.index("Rio Negro") # recuperamos el indice del elemnto que especificamos
print(indice)
provinElim.append(provinList.pop(indice)) # guarda el elemento borrado usando el indice en una nueva lista
print(provinList)
print(provinElim)
del provinList[1:3]           # elimina elemento desde-hasta una posición
print(provinList)

provinList.append("Tucuman")
provinList.append("Tucuman")
print(provinList)
provinList.remove("Tucuman")  # elimina un elemnto específico de la lista sin conocer su ubicacion
print(provinList)
#print("Elemento de lista eliminado: ",provinElim)  # mostramos la lista nueva con elementos eliminados
"""
