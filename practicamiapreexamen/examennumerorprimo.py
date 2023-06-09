
numeroingresado=int(input("ingrese un numero entero y le digo si es primo"))
divisor=numeroingresado-1
esprimo=True

while divisor!=1:
    resto=numeroingresado % divisor 
    
    if resto!=0:
        divisor=divisor-1
    elif resto==0:
        esprimo=False
        divisor=1

if esprimo==True:
    print("Es primo")
else:
    print("no es primo")    