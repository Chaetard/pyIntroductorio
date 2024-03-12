def tamanoAprox(orga, porc, dias,):
    return orga + ((orga * (porc/100)) * dias)

var1 = int(input("Numero inicial de organismos: "))
var2 = int(input("Incremento diario promedio: "))
var3 = int(input("Numero de dias para multiplicar: "))

print(tamanoAprox(var1,var2,var3))



