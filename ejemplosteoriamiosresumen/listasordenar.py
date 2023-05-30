provinList = ["Buenos Aires", "La Pampa", "Rio Negro", "Corrientes", "Entre Rios","Mendoza", "Misiones"]

print(sorted(provinList))      # ordena temporalmente la lista
print(provinList)

print(sorted(provinList, reverse=True))  # ordena de forma descendente de forma temporal

provinList.sort()              # ordena de forma definitiva la lista
print(provinList)

provinList.sort(reverse=True)  # ordena de forma inversa
print(provinList)