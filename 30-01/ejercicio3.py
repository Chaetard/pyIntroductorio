#         #  0   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18  19
enteros = [10,20,30,40,50,60,70,200,90,1,2, 3, 4, 5, 6, 7, 8, 9, 643, 323]
sumaPares = 0
mayorImpar = 0
mayorPar = 0
posicionMayorPar = 0


for i in range (len(enteros)):
   
    
     if (i % 2) == 0:
          sumaPares = enteros[i] + sumaPares
          if(enteros[i] > mayorPar):
              mayorPar = enteros[i]
              posicionMayorPar = i
              
          
     else :
         if(enteros[i] > mayorImpar):
             mayorImpar = enteros[i]
              

print("La suma de ls numeros impares es de: ",sumaPares)
print("El mayor numero impar fu el: " , mayorImpar)  
print("La posicion del numero ",mayorPar," el cual es el numero par mas grande es la posicion: " ,posicionMayorPar)  
