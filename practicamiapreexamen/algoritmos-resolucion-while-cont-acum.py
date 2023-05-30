#1)Mostrar el incremento de cant desde 1 a 100 utilizando while y otra usando for.
"""
cant = 1
while cant <= 100:
    print(cant)
    cant = cant + 1
print("Ahora comienza For:")
for cant in range(1,101):
    print(cant)
"""

# 11) Calcular el promedio de notas obtenidas por un alumno, teniendo 7 notas en el año.
"""
vueltas=1
sumanotas=0
while vueltas<=7:
    nota=float(input("ingrese la nota numero {}: ".format(vueltas)))
    sumanotas=sumanotas+nota
    promedio=sumanotas/7    
    vueltas=vueltas+1
promedio=sumanotas/7
print(int(promedio))
"""

#13) Se pide determinar la calificación final de un examen, teniendo un nro de respuestas
#correctas que suman 4 puntos c/u, un nro de respuestas incorrectas que restan 1 punto c/u
#y un nro de respuestas en blanco.
#aclaracion: la calificacion de la rta se ingresa por teclado
"""
salida=False
cantdecorrectas=0
cantdeincorrectas=0

while salida==False:
    rta=input("ingresa la letra 'c' si la rta es correcta, 'i' si es incorrecta, 'b' si no respondio, y 's' para salir")
    if rta=="c":
        cantdecorrectas=cantdecorrectas+1
    elif rta=="b":
        cantdeincorrectas=cantdeincorrectas+1
    else:
        if rta=="s":
            salida=True
notafinal=(cantdecorrectas*4)+(cantdeincorrectas*(-1))
print(notafinal)

"""

# 22) Dadas 10 notas ingresadas, informar cuántos aprobaron (se aprueba con 4)
"""
aprobados=0
vueltas=0
while vueltas < 10:
    nota=float(input("ingrese nota"))
    if nota >= 4:
        aprobados=aprobados+1
    vueltas=vueltas+1    

print(aprobados)
"""
# 23) Ingresar un nro y mostrar su tabla de multiplicacion
"""
numero=int(input("ingresa un numero"))
vuelta=0
while vuelta <= 10:
    resultado = numero * vuelta
    print(str(numero)+" por "+str(vuelta)+" igual "+str(resultado))
    vuelta=vuelta+1
"""
# 24) Ingresar cantidad de empleados de una empresa. Determinar cuantos ganan mas de 5000, 
# cuantos menos y el costo de la empresa en sueldos.
""""
cantdeemp=int(input("ingresa cant de emp"))
vuelta=0
contadorgananmas=0
contadorgananmenos=0
while vuelta<cantdeemp:
    sueldo=int(input("ingrese sueldo del emp"))
    if sueldo>5000:
        contadorgananmas=contadorgananmas+1
    else:
        contadorgananmenos=contadorgananmenos+1
    vuelta=vuelta+1
print("los que ganan mas son "+str(contadorgananmas)+" y los que menos son "+str(contadorgananmenos))
"""    


# 33) Elaborar un algoritmo que solicite el ingreso de una letra hasta que el operador 
# ingrese un vocal.
"""
vocal=False
while vocal==False:
    letra=str(input("ingrese una letra"))
    vocal=False
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u":
        vocal=True
"""
# 34) Calcular y Mostrar la serie Fibonacci hasta el 100. 
# (cada número es la suma de los dos precedentes, 
# comenzando por 0 y 1). Entonces: 011235..
"""
n1=0
n2=1
acumulador=0

while acumulador<=100:
    print(str(acumulador))
    n1=n2
    n2=acumulador
    acumulador=n1+n2
"""
    
    

