# Aprendemos sobre diccionarios
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

print(MiAgenda)

#Agregar clave y valor
MiAgenda["Ingresos"] = 20000  # agregamos la clave Ingresos con un valor
print(MiAgenda)

#Eliminamos una clave pero antes guardamos en variable
nuevaVar = MiAgenda.pop("Nombres de mascotas")  # tambien se puede subindicar [0:1]
print("Elemento eliminado: ", nuevaVar)
print(MiAgenda)

#Eliminamos clave y valor
del(MiAgenda["Nombre"])   # Para eliminar un par (clave:valor)
print(MiAgenda)

#Eliminamos valor en posicion 0 sin borrar la clave 
del(MiAgenda["Padres"][0:1])  # para eliminar solo un valor de una lista
print(MiAgenda)






