#3)Crear una función en Python que tome como argumento
#un entero que indique la cantidad de términos y retorne
#una lista como la anterior. Por ejemplo:
#>>> fib(10)
#[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
#La función debe, además, chequear que el argumento
#pasado sea mayor a 2. En caso de ser menor, debe
#mostrar un mensaje en pantalla y no retornar nada.
#>>> fib(1)
#La cantidad debe ser mayor a 2.

"""asi agrego elementos al final de la lista
listadefibo=[]
listadefibo.append("hola")
print(listadefibo)
"""
""" Asi consulto el elemento de una lista usando el indice
listaej = [8, 20, 5]
valor = listaej[1] # recuperamos el valor del elemento con el indice
print(valor)
"""

listadefibo=[0,1]
numerodado = int(input("tirame un numero mayor que 2 : "))
elementosqueyatienelalista=len(listadefibo)
vueltas = numerodado-elementosqueyatienelalista

for elementodelalista in range(vueltas):
    n1= listadefibo[len(listadefibo)-1]
    n2= listadefibo[len(listadefibo)-2]
    sumaultimos2= n1+n2
    listadefibo.append(sumaultimos2)
    
print(listadefibo)