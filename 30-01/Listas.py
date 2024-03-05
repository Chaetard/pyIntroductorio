# listasEnteros = [1, 2, 3, 4, 5]
# listasLetras = ['a', 'b', 'c']

# print("Iterando Sobre Enteros")
# for i in range (len(listasEnteros)):
#     print(listasEnteros[i])
   
   
# print("Iterando Sobre Letras")   
# for i in range (len(listasLetras)):
#     print(listasLetras[i])
        
        
# grados = [[12.2,11.1,11.4,10.3,9.2,20.1,21.1,22.43,23.4,22.3,22.2,23.23,12.2,11.1,11.4,10.3,9.2,20.1,21.1,22.43,23.4,22.3,22.2,23.23, ], ["0 am", "1 am", "2 am", "3 am", "4 am", "5 am", "6 am", "7 am", "8 am", "9 am", "10 am", "11 am", "12 pm", "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm", "7 pm", "8 pm", "9 pm", "10 pm", "11 pm"]]


# masAlto = 0
# masBajo = 100
# posicion = 0
# posicion2 = 100

# mediaSuma = 0

# for row in grados[0]:
#     if row > masAlto:
#         masAlto = row
#         posicion = grados[0].index(row)
#     if row < masBajo:
#         masBajo = row
#         posicion2 = grados[0].index(row)
    
#     mediaSuma = mediaSuma + row
     
        

# print("La temperatura mas alta fue de: ", masAlto, " a las: ", grados[1][posicion])
# print("La temperatura mas baja fue de: ", masBajo, " a las: ", grados[1][posicion2])


# print("y la media fue de ", mediaSuma/(len(grados[0])))




# diasTemperatura = [[25.23,32.21,29.1,32.1,27.3,32.5,28.3],["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]]
# promedio = 0

# for row in diasTemperatura[0]:
#     promedio = promedio + row

# promedio =  promedio/(len(diasTemperatura[0]))


# print("el promedio es de:", promedio)

# dias = []

# if row > masAlto:
#         masAlto = row
#         posicion = grados[0].index(row)
#     if row < masBajo:
#         masBajo = row
#         posicion2 = grados[0].index(row)
    
#     mediaSuma = mediaSuma + row

# masAlto = 0
# masBajo = 100
# posicion = 0
# posicion2 = 0

# for i in range (len(diasTemperatura[0])):
#     dias.append(diasTemperatura[0][i] - promedio)
#     print("la diferencia con el promedio del dia: ", diasTemperatura[1][i], " es de: ", dias[i])
#     if diasTemperatura[0][i] > masAlto:
#         masAlto = diasTemperatura[0][i]
#         posicion = diasTemperatura[1][i]
        
#     if diasTemperatura[0][i] < masBajo:
#         masBajo = diasTemperatura[0][i]
#         posicion2 = diasTemperatura[1][i]
#         print(diasTemperatura[1][i])


# print("la tempertatura mas alta fue de: ", masAlto , " y fue el dia:",posicion)
# print("la temperatura mas baja fue de:", masBajo, " y fue el dia:", posicion2)

#         #  0   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18  19
# enteros = [10,20,30,40,50,60,70,200,90,1,2, 3, 4, 5, 6, 7, 8, 9, 643, 323]
# sumaPares = 0
# mayorImpar = 0
# mayorPar = 0
# posicionMayorPar = 0


# for i in range (len(enteros)):
   
    
#      if (i % 2) == 0:
#           sumaPares = enteros[i] + sumaPares
#           if(enteros[i] > mayorPar):
#               mayorPar = enteros[i]
#               posicionMayorPar = i
          
#      else :
#          if(enteros[i] > mayorImpar):
#              mayorImpar = enteros[i]
              

# print("La suma de ls numeros impares es de: ",sumaPares)
# print("El mayor numero impar fu el: " , mayorImpar)  
# print("La posicion del numero ",mayorPar," el cual es el numero par mas grande es la posicion: " ,posicionMayorPar)  


# enteros = [10,20,30,40,50,60,70,200,90,1,2, 3, 4, 5, 6, 7, 8, 9, 643, 323,10,20,30,40,50,60,70,200,90,1]
# sumaPares = 0
# sumaImpares = 0

# for i in range (len(enteros)):
#      if (i % 2) == 0:
#          sumaPares = sumaPares + enteros[i]
#          print("pares")
         
#      else: 
#          sumaImpares = sumaImpares + enteros[i]
#          print("impares") 
         
         
# print("La suma de los numeros en posiciones pares es de: " ,sumaPares)
# print("la suma de los numeros en posiciones impares es de: " ,sumaImpares)
# print("La suma de todos los elementos es de: " ,(sumaImpares + sumaPares)) 


contadorCero = 0
contadorPositvos = 0
contadorNegativos = 0
positivosSuma = 0
negativoSumas = 0
listaNumeros = [0,5,-2,15,93,0,-23,-45,43,54,0,0,32,-43,-54]
for i in range (len(listaNumeros)):
    if(listaNumeros[i] == 0):
        contadorCero +=1
    elif(listaNumeros[i]  > 0):
        contadorPositvos += 1
        positivosSuma += listaNumeros[i]
        
    else: 
        contadorNegativos += 1
        negativoSumas += listaNumeros[i]
        
        
print("la suma de los es de: begativos " ,negativoSumas)
print("la sumad de los positivos es de ", positivosSuma)
print("hay ", contadorCero, " ceros en la cadena")
print("hay " , contadorNegativos , " negativos")
print(" hay ", contadorPositvos , "positivos")        
           
        
        