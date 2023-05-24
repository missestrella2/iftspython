serie = [0,1]   # 0 1 1 2 3 5 
uno = 0
dos = 1
tres = 0

######### Agregar elementos a la lista
serie.append(tres)    # la serie en formato lista
print(serie)

otro = "bla"
serie.append(otro)
print(serie)

meh = otro + str(dos)  # la serie en formato string
serie.append(meh)
print(serie)

serie.insert(2,"Rio Negro") # inserta "Rio Negro" en la posicion 2 contando desde 0
print(serie)

########## Eliminar elementos a una lista

provinList = ["Buenos Aires", "La Pampa", "Rio Negro", "Corrientes", "Entre Rios","Mendoza", "Misiones"]

del provinList[2]              # elimino el elemnto que este en la posición 2
print(provinList)

del provinList[-1]             # eliminamos un elemnto desde el final de la lista
print(provinList)

del provinList[1:3]           # elimina elemento desde-hasta una posición
print(provinList)

provinList.remove("Mendoza")  # elimina un elemnto específico de la lista sin conocer su ubicacion
print(provinList)

elimProv = provinList.pop(1)  # elimina el elemento 1 pero antes guarda el elemento borrado en una variable
print(provinList)
print(elimProv)

