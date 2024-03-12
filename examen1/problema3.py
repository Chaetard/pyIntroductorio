def rectangulo():
    var1 = int(input("base: "))
    var2 = int(input("altura: "))
    return(var1 * var2)
print("ingrese las medidas del primer rectangulo")
rectangulo1 = rectangulo()
print("ingrese las medidas del segundo")
rectangulo2 = rectangulo()

print("El mayor es el primero" if rectangulo1 > rectangulo2 else "El mayor es el segundo")

 