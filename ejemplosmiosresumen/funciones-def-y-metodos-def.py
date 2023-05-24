# diferencia entre METODOS y FUNCIONES
# una funcion se la puede llamar directamente
# puede tener o no parametros
# se puede poner o no return
# el return siempre esta implicito, si no se pone es como poner "return None"

#EJEMPLOS DE FUNCIONES

#funcion sin parametros
#sin return
#----------------
def di_hola():
    print('Hello')
#----------------
di_hola()

#funcion con parametros
#sin return
#----------------
def saludo(nombre):
    print(f"Hola {nombre}")
#----------------        
saludo("Timmy")

#funcion sin parametros
#con return
#----------------
def funcion(a):
  return a
#----------------
bla = funcion(12)  ### aca llamo a la funcion y le paso un valor entre los parentesis
print(bla)

#funcion con parametros
#con return

def funcion(a):
  return a

bla = funcion(12)  ### aca llamo a la funcion y le paso un valor entre los parentesis
print(bla)


def dividir (dividendo, divisor=2):
	resultado = dividendo/divisor
	return resultado
 

