##PROBADNO COSAS PARA EL FUTURO PROYECTO

#diccionario de productos
stock={
        1:{
            "producto":"pan lactal 200g",
            "precio":"45",
            },
        2:{
            "producto":"tomate por unidad",
            "precio":"32",
            },
        }

acumulador=0

#Ingresar el codigo de un producto y la cantidad y que me diga el subtotal de ese producto
#RECORDAR AGREGAR EN CADA INPUT LA VALIDACION1!

codigo = int(input("Ingrese codigo")) 
cantidad = int(input("ingrese cantidad"))
preciounitario = stock[codigo]["precio"] #asi consulto el elemento de un subdiccionario usando las key
preciosubtotal = float(preciounitario) * float(cantidad)
subtotalproducto = print("producto: {}, precio: {}, cant: {}, subtotal: {}".format(stock[codigo]["producto"],stock[codigo]["precio"],cantidad,preciosubtotal))
acumulador = acumulador+preciosubtotal
subtotaldetodo=print("Subtotal de la cuenta: {}".format(acumulador))

# recordar crear un diccionario que va a ser el ticket
# aca hacer que guarde el ultimo producto como un diccionario dentro del diccionario ticket
# cada elemento del diccionario ticket va a ser una LINEA que contiene precio, cantidad, nombre del prod etc

#aca habria que decidir la condicion para salir del bucle y totalizar la cuenta

#total de la cuenta (iria fuera del bucle de pedir producto por producto)
#aca hay que hacer esto: 
# 1 que imprima el ticket con todo bien alineado con format
# 2 que recorra el diccionario ticket y sus elementos LINEA 1, LINEA 2, LINEA 3

print("Total: {}".format(acumulador))

#ejemplo de internet para usar format en la impresion del ticket
#:>10d   Entero alineado a la derecha en un campo de 10 caracteres
#:<10d   Entero alineado a la izquierda en un campo de 10 caracteres
#:^10d   Entero centrado en un campo de 10 caracteres
#:0.2f   Flotante con dos dígitos de precisión

print("Ejemplo sacado de internet de texto alineado, esto tenemos que lograr")

for i in range (6):
    nombre = 'Naranja'
    cajones = 100
    precio = 91.1
    print(f'{nombre:>10s} {cajones:>10d} {precio:>10.2f}')


## cosas a revisar y a tener en cuenta,preguntar a la profe
## y si quiero anular un producto? hay que hacerlo? si hay que hacerlo primero lograr que funcione lo basico y despues incorporar el borrado
## hay que dar de alta productos?
## hay que poner medios de pago diferentes?
## el programa finaliza cuando se termina de facturar o queda listo para poder facturar despues?
## tiene que llevar fecha, direccion del negocio, etc? o algun otro dato adicional? 
## se puede anular tickets, reimprimirlos, etc?
## los tickets tambien hay que ir guardandolos? 

## usaria esta estructura:
## funcion pedircodigo: ingresar codigo y su validacion
## funcion pedircantidad: ingresar la cantidad y su validacion
## funcion subtotallinea: imprime los subtotales del producto
## funcion guardarlinea: guarda los datos de codigo, nombre producto, cantidad y subtotal en un dicc 
## funcion facturaproducto: llama a la f pedircodigo,pedircantidad,subtotalinea,guardarlinea y repite (bucle)
## funcion imprimirticket: llama al dicc que tiene las lineas de ticket y las imprime. tambien suma el total de todo 

##el programa seria llamar a la funcion facturarproducto, luego a la de imprimirticket