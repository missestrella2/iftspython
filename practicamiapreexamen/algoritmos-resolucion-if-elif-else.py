# 28) Elabore un algoritmo que solicite la edad de dos hermanos y 
# muestre un mensaje indicando la edad del mayor y cuántos años
# de diferencia tiene con el menor.
'''
hno1=int(input("ingresa edad de hno1"))
hno2=int(input("ingresa edad de hno2"))
if hno1<hno2:
    print(hno2-hno1)
elif hno1>hno2:
    print(hno1-hno2)
else:
    print("0")
'''
# 29) Se tiene registrada la producción (en unidades) lograda por un operario 
# a lo largo de la semana (lunes a sabado).
# Elabore un algoritmo que nos diga si el operario recibirá incentivo por productividad,
# sabiendo que el promedio de producción mínima es de
# 100 unidades semanales.
"""
prodlunes=20
prodmartes=10
prodmiercoles=30
prodjueves=10
prodviernes=10
prodsabados=2
sumaprod=prodlunes+prodmartes+prodmiercoles+prodjueves+prodviernes+prodsabados

if sumaprod>=100:
    print("recibe incentivo")
else :
    print("no recibe incentivo")
"""
# 30) Elabore un algoritmo para 
# leer 3 numeros enteros diferentes entre sí y determinar el número mayor de los 3.
"""
numero1=5
numero2=42
numero3=300

if numero1 > numero2 and numero1 > numero3:
    print("el mayor es "+str(numero1))
elif numero2 > numero1 and numero2 > numero3:
    print("el mayor es "+str(numero2))
else:    
    print("el mayor es "+str(numero3))
"""

# 31) Elabore un algoritmo que solicite la edad de 200 personas y muestre 
# cuántas son mayores y cuántas menores de edad.
"""
contadormayores=0
contadormenores=0
for personas in range(3):
    edad=int(input("ingrese edad"))
    if edad<18:
        contadormenores=contadormenores+1
    else:    
        contadormayores=contadormayores+1
print("mayores: "+str(contadormayores)+", menores:"+str(contadormenores))
"""