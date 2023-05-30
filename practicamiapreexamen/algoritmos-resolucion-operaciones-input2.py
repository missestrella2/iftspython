#7) Escriba un algoritmo que pida una distancia en pies y pulgadas y 
#que escriba dicha distancia en centímetros. 
#Se recuerda que 
#1 PIE = 12 pulgadas 
#1 pulgada = 2,54 cm
"""
dpies = float(input("ingresa distancia en pies"))
piesapulgadas=dpies*12
pulgadasacm=piesapulgadas*2.54 
print(pulgadasacm)

dpulgadas = float(input("ingresa distancia en pulgadas"))
pulgadasacm2=dpulgadas*2.54 
print(pulgadasacm2)
"""
#8) Escriba un algoritmo que pida una temperatura en grados Celsius y que convierta dicha
#temperatura en grados Fahrenheit. Se recuerda que la relacion entre grados Celsius (C)
# y grados Fahrenheit (F) es la siguiente: F = 1,8 * C + 32.
"""
gcelsius = int(input("ingresa temperatura en grados Celsius"))
gfarenheit = 1.8 * gcelsius + 32
print(gfarenheit)
"""
# 9) Escriba un algoritmo que pregunte al usuario el número de horas trabajadas y el costo
# por hora. Determinar el pago de jornal que le corresponde.
"""
hstrabajadas = float(input("ingresa hs trabajadas"))
costoporhora= float(input("ingresa costo de la hora"))
jornal=hstrabajadas*costoporhora
print(jornal)
"""
# 10) Calcular la distancia recorrida por un auto a velocidad constante y en un tiempo
# determinado. Tener en cuenta la fórmula de Movimiento Rectilineo Uniforme:
# Distancia = Velocidad * Tiempo 
"""
velocidad=float(input("ingresa velocidad en km/h"))
tiempo=float(input("ingresa horas"))
distancia=velocidad*tiempo
print(distancia)
"""
# 11) Calcular el promedio de notas obtenidas por un alumno, teniendo 7 notas en el año.
"""
nota1=float(input("ingresa nota 1"))
nota2=float(input("ingresa nota 2"))
nota3=float(input("ingresa nota 3"))
nota4=float(input("ingresa nota 4"))
nota5=float(input("ingresa nota 5"))
nota6=float(input("ingresa nota 6"))
nota7=float(input("ingresa nota 7"))
suma=(nota1+nota2+nota3+nota4+nota5+nota6+nota7)
promedio=suma/7
print(promedio)
"""
# 12) Escribir un algoritmo que pregunte al usuario una cantidad a invertir, el interes anual,
# y el numero de años. Mostrar el capital obtenido en la inversión.
"""
cantidadainvertir=float(input("ingresa cantidad a invertir"))
interesanual=float(input("ingresa interes anual"))
numerodeanios=float(input("ingresa numero de años"))
interestotal=numerodeanios*(interesanual*cantidadainvertir/100)
capital=cantidadainvertir + interestotal
print(capital) 
"""
#13) Se pide determinar la calificación final de un examen, teniendo un nro de respuestas
#correctas que suman 4 puntos c/u, un nro de respuestas incorrectas que restan 1 punto c/u
#y un nro de respuestas en blanco.
"""
respuestascorrectas=2
respuestasincorrectas=5
respuestasenblanco=3
puntosrespuestascorrectas=4
puntosrespuestasincorrectas=1
puntosrespuestasenblanco=0
nota=(respuestascorrectas*puntosrespuestascorrectas)-(respuestasincorrectas*puntosrespuestasincorrectas)+(respuestasenblanco*puntosrespuestasenblanco)
print(nota)
"""

# 27) Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
# Suele hacer venta por correo y la empresa de logística
# les cbra por peso de cada paquete, asi que deben calcular el peso de los payasos 
# y muñecas que saldrán en cada paquete a demanda. Cada payaso 
# 11,5 kg y cada muñeca 7,5 kg. Escribir un programa que lea el numero de payasoss 
# y muñecas vendidos en el último pedido y calcule el peso
# total del paquete que será enviado.
"""
pesopayaso= 11.5
pesomunieca=7.5
cantidaddepayasos=3
cantidaddemuniecas=2

print("peso de payasos: "+str(cantidaddepayasos*pesopayaso))
print("peso de muñecas: "+str(cantidaddemuniecas*pesomunieca))
"""
