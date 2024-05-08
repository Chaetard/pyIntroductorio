cadena = "AAAIISSIIOOO"
cadena1 = list(cadena)
contador = 0


def suma(entero:int , entero2:int) -> int:
    sumaRes = entero + entero2
    return sumaRes

print(suma(0,len(cadena1)))


entero = suma(0,len(cadena1))


for i in range(entero):
    
    if cadena1[i] == "I":
        contador += 1
        print("Encontre la i en el posicion: ", i + 1 )




      
               
print("I optenidas: " , contador)

