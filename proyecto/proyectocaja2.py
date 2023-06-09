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

indice=0
contador=0

prodval=list(stock.values())
prodkey=list(stock.keys())
#print(prodkey[0])
#print(prodval[0])
print("Codigo,Producto,Precio")
for productos in stock:
    print("{},{},{}".format((prodkey[contador]),(prodval[contador]["producto"]),(prodval[contador]["precio"])))
    contador=contador+1

acumulador=0
subtotalproducto=0
sigue=True
#PRODUCTO 1
while sigue==True:
    codigo = int(input("Ingrese codigo")) 
    cantidad = int(input("ingrese cantidad"))
    preciounitario = stock[codigo]["precio"] #asi consulto el elemento de un subdiccionario usando las key
    preciosubtotal = float(preciounitario) * float(cantidad)
    subtotalproducto = print("producto: {}, precio: {}, cant: {}, subtotal: {}".format(stock[codigo]["producto"],stock[codigo]["precio"],cantidad,preciosubtotal))
    acumulador=acumulador+preciosubtotal
    mas=input("Ingresa mas productos? s/n")
    if mas=="s":
        sigue=True
    elif mas=="n":
        sigue=False

subtotaldetodo=print("Subtotal de la cuenta: {}".format(acumulador))

print("Total: {}".format(acumulador))