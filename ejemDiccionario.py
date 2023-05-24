# Aprendemos sobre diccionarios
NuevoDic = dict()
NuevaLista = list()
NuevaTupla = tuple()
OtroDict = {}
OtraLista = []
OtraTupla = ()
#
MiAgenda = {
'Nombre' : "Maria",
'Apellido' : "Perez",
'Alias' : "Mery",
'Padres' : ["Maria Gomes", "Carlos Perez"], #<-- esto es una lista
'Edad' : 55,
'Genero' : "Femenino",
'Estado Civil' : "Soltera",
'Hijos' : ("Juan", "Pedro", "Tomas", "Carla"),  # esto es una tupla
'Mascotas' : "Gatos",
'Nombres de mascotas' : ["Mishu", "Pompon"] #<-- esto es una lista
}
#print(MiAgenda)
print("la edad de ", MiAgenda["Apellido"], " es: ", MiAgenda["Edad"])
#print(MiAgenda["Apellido"])
#print(MiAgenda["Padres"][0:2])
#print(MiAgenda["Hijos"][0:3])
#MiAgenda["Ingresos"] = 20000  # agregamos la clave Ingresos con un valor
#print(MiAgenda)
#print(MiAgenda["Ingresos"])
#print(MiAgenda["Nombres de mascotas"][1:2])
#nuevaVar = MiAgenda.pop("Nombres de mascotas")  # tambien se puede subindicar [0:1]
#print("Elemento eliminado: ", nuevaVar)
#print(MiAgenda)
#del(MiAgenda["Nombre"])   # Para eliminar un par (clave:valor)
#print(MiAgenda)
#del(MiAgenda["Padres"][0:1])  # para eliminar solo un valor de una lista
#print(MiAgenda)
#MiAgenda["Salario"] = MiAgenda.pop("Ingresos")  # creamos la clave Salario y eliminamos Ingresos
#print(MiAgenda["Salario"])
#print(MiAgenda)
#print(MiAgenda.get("Nombre", "No existe Nombre")) # obtiene el valor de un elemento o muestra mensaje que definimos
#claves = MiAgenda.keys()
#print(type(claves))
#valores = MiAgenda.values()
#print(valores)

lista = [("semana","lunes"),("Meses","Junio"),("Campo", "nuevo")]
nuevoDiccio = {
"semana": "lunes",
"Meses": "Junio"}
#print(nuevoDiccio)
#nuevoDiccio = {clave:valor for clave, valor in lista} # estoy creando un dic tomando el primer valor como clave y el segundo como valor
#print(nuevoDiccio)
#claves = nuevoDiccio.keys()
#print(claves)
#valores = nuevoDiccio.values()
#print(valores)
## creamos un diccionario con listas fucionadas usando zip()
nLista = ["Pedro", "Juan", "Tomas", "Payasos"]
eLista = [32,40,28,("Gaby","Fofo", "Miliki")]
diccio = dict(zip(nLista, eLista))
#print(diccio)
newDicc = {
'Meses': ["Enero", "Febrero", "Marzo"],
'Edades': dict(zip(nLista, eLista)),
}
#print(newDicc)
#print(newDicc["Edades"]["Payasos"][1:2])  # accedo al valor del subDicionario
"""
claves = MiAgenda.keys()
print(claves)
valores = MiAgenda.values()
print(valores)
print("aqui vienen las claves y luego valores...")
for ind in claves:
	print(ind)
for ind in valores:
	print(ind)
"""
