# Aprendemos sobre diccionarios
MiAgenda = {
'Nombre' : "Maria",
'Apellido' : "Perez",
'Padres' : ["Maria Gomes", "Carlos Perez"], 
}

#consultar valor usando la key
print(MiAgenda["Apellido"])
print(MiAgenda["Padres"][0:2])

# consultar valor usando la key o muestra mensaje que definimos
print(MiAgenda.get("Nombre", "No existe Nombre")) 

#imprimo todas las claves (sin sus valores)
claves = MiAgenda.keys()
print(claves)
#recorro claves con un for
for ind in claves:
	print(ind)

#imprimo todos los valores (sin sus claves)
valores = MiAgenda.values()
print(valores)
#recorro values con un for	
for ind in valores:
	print(ind)
	
#Consultar un diccionario dentro de otro (subdiccionario)

newDicc = {
'Meses': ["Enero", "Febrero", "Marzo"],
'Edades': {'Pedro': 32, 'Payasos': ('Gaby', 'Fofo')}
}

print(newDicc)
print(newDicc["Edades"]["Payasos"][1:2])  # accedo al valor del subDicionario 

