#esta lista esta formada por pares de valores
lista = [("semana","lunes"),("Meses","Junio"),("Campo", "nuevo")]

# estoy creando un dic tomando el primer valor como clave y el segundo como valor
nuevoDiccio = {clave:valor for clave, valor in lista} 
print(nuevoDiccio)

