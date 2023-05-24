#IMPORTANTE: LAS TUPLAS SON INMUTABLES

#Definir tupla
nuevaTupla = tuple()
mesTupla = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Sept", "Oct", "Nov", "Dic")
mesSemana = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

print(mesTupla)

#si sumo tuplas las une poniendo una seguida de la otra
ejemTupla = mesTupla + mesSemana
print(ejemTupla)

#consultar usando el indice del elemento
mesRecuperado = mesTupla[3]
print("Me guarde la posición 3 de la tupla: ", mesRecuperado)

#usamos type que devuelve el tipo de elemento
print(type(mesTupla))