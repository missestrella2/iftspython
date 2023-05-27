# Ejemplos de Range()
#range(start,stop,step)
    #las variuables de range son asi:
        #start: en donde empieza (incluido)
        #stop: en donde termina (no incluido)
        #step: incremento, de cuanto en cuanto salta
#se puede usar range con uno, dos o los tres argumentos
#lo puedo inprimir en forma de lista o con un buble for


#imprimir lista que va del 0(incluido)  al 2 (no incluido) 
#range(2)
for e in range(2):
    print(e)   

#va del 1(incluido) al 4 (no incluido)
#range(1,4)
bla=list(range(1,4))
print(bla)

#va del numero 2(incluido) al 27(no incluido) y de 3 en 3
#range(2, 27, 3) # Inicio, Fin, Incremento
for e in range(2,27,3):
    print(e)   

