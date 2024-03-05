votos = [["distrito", "candidato A", "candidato B", "candidato C","candidato D"],
         [1, 94, 48, 206, 45],
         [2,180,20,320,16],
         [3,221,90,140,20],
         [4,432,50,821,14],
         [5,820,61,946,18],]

sumaA = 0
sumaB = 0
sumaC = 0
sumaD = 0
sumaTotal = 0

eleccion50 = False

sumasArreglo = []

elecciones = 0
eleccionesCandidato1 = 0

elecciones2 = 0
eleccionesCandidato2 = 0


contador = 0

for i in range(len(votos)):
    for j in range(len(votos[i])):
        contador += 1
        print("{:<15}".format(votos[i][j]), end=" ")
        if((contador%5) == 0):
        
            print("")
        
        if(j >= 1 and i >= 1 and j <= 4 and i <= 5):
            if(j == 1):
                sumaA += votos[i][j]
                sumasArreglo.append(sumaA)
            if(j == 2):
                sumaB += votos[i][j]
                sumasArreglo.append(sumaB)
            if(j == 3):
                sumaC += votos[i][j]
                sumasArreglo.append(sumaC)
            if(j == 4):
                sumaD += votos[i][j]
                sumasArreglo.append(sumaD)
            
            
sumaTotal  = sumaA + sumaB + sumaC + sumaD   


for i, suma in enumerate([sumaA, sumaB, sumaC, sumaD]):
                if (suma > eleccionesCandidato1):
                    eleccionesCandidato2 = eleccionesCandidato1
                    eleccionesCandidato1 = suma
                    elecciones = votos[0][i + 1]
                elif (suma > eleccionesCandidato2):
                    eleccionesCandidato2 = suma
                    elecciones2 = votos[0][i + 1]     
    
print("El candidato con mas votos es: ",elecciones)
print("La suma de los votos del candidato A es de: ",sumaA)
print("La suma de los votos del candidato B es de: ",sumaB)
print("La suma de los votos del candidato C es de: ",sumaC)
print("La suma de los votos del candidato D es de: ",sumaD)
print("El total de votos es de: ", sumaTotal)

contador = 0
sumaTotal = 100/sumaTotal
for i in range(len(sumasArreglo)):
    if((sumasArreglo[i] * sumaTotal) > 50 and i >= 15):
        contador = i - 15
        print("Hay ganador")
        print("El ganador es el candidato: ",votos[0][contador])
        eleccion50 = True
        
        

        
                    
if(eleccion50 == False):
    print("Hay segunda ronda de elecciones")
    print("El candidato con mas votos es: ",elecciones)
    print("El candidato con el segundo lugar es: ",elecciones2)       
                