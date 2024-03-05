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
           