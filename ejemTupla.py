# ejemplo de tuplas
mesLista = ["uno","dos", "tres", "cuatro", "cinco", "seis", "ocho", "nuevo", "diez"]
nueLista = [1,2,3,4,5,6,7,8,9,10]
newTupla = tuple()
mesTupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Sept", "Oct", "Nov", "Dic")
mesSemana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")
"""
print(mesTupla)
ejemTupla = mesTupla + mesSemana
print(ejemTupla)
concaLista = mesLista + nueLista
print(concaLista)
"""
mesRecuperado = mesTupla[3]
print("Me guarde la posición 3 de la tupla: ", mesRecuperado)
print(mesTupla[4])
print(type(mesTupla))
print(type(mesLista))
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
print(type(MiAgenda))
otro1 = 0
otro2 = "mio"
otro3 = True
print(type(otro1))
print(type(otro2))
print(type(otro3))
