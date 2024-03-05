#Ejercicio de listas de dos dimenciones

lista = [[83,93,23,54,72],[72,32,65,21,87],[43,54,87,12,65]]

listaSusana = 0

puntajeSociales = 0
indiceSociales = 0

for i in range(3):
    for j in range(5):
        if(j == 4):
            listaSusana += lista[i][j]
        if(puntajeSociales >= lista[1][j]):
            puntajeSociales = lista[1][j]
            
        
        


print("El promedio de Susana es de : ", (listaSusana / 3))
print(puntajeSociales)