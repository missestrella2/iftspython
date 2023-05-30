# FUNCIONES
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
def funcion():
  hola="palabra"
  return hola
#----------------
bla = funcion()  ### aca llamo a la funcion y guardo el resultado en la variable bla
print(bla)       ### recordar que solo la guarde pero si no pongo print no la imprime 

#funcion con parametros
#con return
def funcion(a):
  return a
#----------------
palabra = funcion("ufa")  ### aca llamo a la funcion, le mando un parametro entre los parentesis y guardo el resultado en la variable palabra
print(palabra)            ### recordar que solo la guarde pero si no pongo print no la imprime 

