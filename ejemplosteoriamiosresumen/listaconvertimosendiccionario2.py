nLista = ["Pedro", "Juan", "Tomas", "Payasos"]
eLista = [32,40,28,("Gaby","Fofo", "Miliki")]

## creamos un diccionario con listas fusionadas usando zip()
#la primer lista da las keys y la segunda lista da los values
diccio = dict(zip(nLista, eLista))

print(diccio)