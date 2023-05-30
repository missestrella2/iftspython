#para pedir ingresos por teclado se usa input

input("ingresa un numero: ")

#si no lo guardamos en una variable el programa se termina y no podemos utilizar esa variable
#asi guardamos en variable: 

n2 = input("ingresa otro numero: ")

#Ahora si me lo guardo pero no le dije que haga nada con ese numero.
#Utilizo esa variable para algo, por ejemplo imprimir:

print(n2)

print("el segundo numero es "+n2)

## OJO CON ESTO
## SI YO AGARRO UN NUMERO Y LO QUIERO CONCATENAR CON UN STRING ME TIRA ERROR
## POR QUE EN ESTE CASO NO ME TIRA ERROR?
## PORQUE TODO LO QUE SE INGRESA A TRAVES DE INPUT SE CONVIERTE AUTOMATICAMENTE EN STRING
# se nota cuando tratamos de sumar el numero ingresado y da error

#suma = 5 + n2 #esto tira error!! porque el n2 es un string

## para evitar el error hay que convertir el string a numero 

suma = 5 + int(n2)

print("5 mas {} es ".format(suma))