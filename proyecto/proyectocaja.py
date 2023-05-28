#diccionario de productos
stock={
        1:{
            "producto":"pan lactal 200g",
            "precio":"34.5",
            },
        2:{
            "producto":"tomate por unidad",
            "precio":"32",
            },
        3:{
            "producto":"arroz x 500g",
            "precio":"21",
           }
        }

acumulador=0

#Ingresar el codigo de un producto y la cantidad y que me diga el subtotal de ese producto
codigo = int(input("Ingrese codigo"))
cantidad = int(input("ingrese cantidad"))
preciounitario = stock[codigo]["precio"]
preciosubtotal = float(preciounitario) * float(cantidad)
subtotalproducto = print("producto: {}, precio: {}, cant: {}, subtotal: {}".format(stock[codigo]["producto"],stock[codigo]["precio"],cantidad,preciosubtotal))
acumulador = acumulador+preciosubtotal
subtotaldetodo=print("Subtotal de la cuenta: {}".format(acumulador))

#aca habria que decidir la condicion para salir del bucle y totalizar la cuenta

#total de la cuenta (iria fuera del bucle de pedir producto por producto)
print("Total: {}".format(acumulador))
