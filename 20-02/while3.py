valor = int(input("ingrese un valor que sera sumado consigo mismo 100 veces: "))
valor2 = valor
cent = 1

while cent <= 99:
    valor = valor + valor2
    cent = cent + 1
    
print("la suma es de: ", valor)