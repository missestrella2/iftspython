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
    
    

