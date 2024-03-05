enteros = [10,20,30,40,50,60,70,200,90,1,2, 3, 4, 5, 6, 7, 8, 9, 643, 323,10,20,30,40,50,60,70,200,90,1]
sumaPares = 0
sumaImpares = 0

for i in range (len(enteros)):
     if (i % 2) == 0:
         sumaPares = sumaPares + enteros[i]
       
         
     else: 
         sumaImpares = sumaImpares + enteros[i]
        
         
print("La suma de los numeros en posiciones pares es de: " ,sumaPares)
print("la suma de los numeros en posiciones impares es de: " ,sumaImpares)
print("La suma de todos los elementos es de: " ,(sumaImpares + sumaPares)) 
