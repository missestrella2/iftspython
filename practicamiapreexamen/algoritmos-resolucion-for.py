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
# aclaracion: ingresando las notas por teclado
"""
sumanotas=0
for notas in range(1,8):
    nota=float(input("ingrese nota numero {}".format(notas)))
    sumanotas=sumanotas+nota
promedio=sumanotas/7
print("el promedio de las 7 notas es {}".format(round(promedio,2)))

"""

#13) Se pide determinar la calificación final de un examen, teniendo un nro de respuestas
#correctas que suman 4 puntos c/u, un nro de respuestas incorrectas que restan 1 punto c/u
#y un nro de respuestas en blanco.
#aclaracion: son 3 respuestas y se ingresan por teclado
"""
suma_resp_cor=0
suma_resp_inc=0

for respuestas in range(3):
    rta = float(input("Rta nro {}: ingrese 1 si la rta es correcta, 2 si es incorrecta, 3 si no respondio".format(respuestas+1)))
    if rta==1:
        suma_resp_cor=suma_resp_cor+1
    elif rta==2: 
        suma_resp_inc=suma_resp_inc+1
notafinal=(suma_resp_cor*4)+(suma_resp_inc*(-1))
print(notafinal)

"""

# 25) Ingresar una cantidad de personas, por cada una: ingresar la estatura y mostrar el 
# promedio de altura final.
"""
#CON WHILE:
cantdepers=int(input("ingresa cant de pers"))
vuelta=1
acumest=0
while vuelta<=cantdepers:
    est=float(input("ingresa est"))
    acumest=acumest+est
    vuelta=vuelta+1
promedio=acumest/cantdepers
print(promedio)
"""
"""
#CON FOR:
cantdepers=int(input("ingresa cant de pers"))
acumest=0
for vuelta in range(cantdepers):
    est=float(input("ingresa est"))
    acumest=acumest+est
    vuelta=vuelta+1
promedio=acumest/cantdepers
print(promedio)
"""
# 26) Dadas 10 letras ingresadas determinar cuál es vocal y cuál es consonante.
"""
#CON WHILE
vuelta=1
while vuelta<=10:
    letra=str(input("ingresa una letra"))
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        print("vocal")
    else:
        print("consonante")
    vuelta=vuelta+1
"""
"""
#CON FOR
for vuelta in range(10):
    letra=str(input("ingresa una letra"))
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        print("vocal")
    else:
        print("consonante")
    vuelta=vuelta+1
"""

# 32) Elaborar un algoritmo para obtener el resultado del escrutinio 
# en las elecciones del delegado escolar. 
# Considerar que hay 160 electores y se han presentado 3 candidatos. 
# Todos votaron, se declara el ganador por
# mayoría simple.
#  En el siguiente link tienen un video con la resolución, explicación y prueba de escritorio:
#  https://drive.google.com/drive/folders/10PpF0CGZunzRP6XImzsJQUadOqAanV5b?usp=share_link
#  (ver tiempo desde 2:32:10 hasta 3:00:00, a partir de 3:42:40 está la prueba de escritorio)

 
#sabiendo la cantidad de votos 
"""
contadorvotoscandidato1=90
contadorvotoscandidato2=30
contadorvotoscandidatos3=40

if contadorvotoscandidato1>contadorvotoscandidato2 and contadorvotoscandidato1>contadorvotoscandidatos3:
    print("gano candidato1")
elif contadorvotoscandidato2>contadorvotoscandidato1 and contadorvotoscandidato2>contadorvotoscandidatos3:
    print("gano candidato 2") 
else:
    print("gano candidato 3")      
"""

#otra solucion, ingresando los votos uno por uno 
"""
contadorvotoscandidato1=0
contadorvotoscandidato2=0
contadorvotoscandidato3=0

for votantes in range(160):
    voto=int(input("ingrese que numero de candidato vota"))
    if voto==1:
        contadorvotoscandidato1=contadorvotoscandidato1+1
    elif voto==2:
        contadorvotoscandidato2=contadorvotoscandidato2+1
    else:    
        contadorvotoscandidato3=contadorvotoscandidato3+1
        
if contadorvotoscandidato1>contadorvotoscandidato2 and contadorvotoscandidato1>contadorvotoscandidato3:
    print("gano candidato1")
elif contadorvotoscandidato2>contadorvotoscandidato1 and contadorvotoscandidato2>contadorvotoscandidato3:
    print("gano candidato 2") 
else:
    print("gano candidato 3")      
"""
