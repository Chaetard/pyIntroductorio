#Ejercicio de listas de dos dimenciones

lista = [[60,90,50,70,100],[20,90,40,90,34],[100,100,90,80,30]]
listaAlumnos = ["juan","pedro","petra","carmen","susana"]
listaMaterias = ["matematicas","sociales","naturales"]


numeroMateriaPetra = 0
numeroMateriaPetraFinal = 0

numeroMateriaJuan = 0
numeroMateriaJuanFinal = 0

puntajeSociales = 0
indiceSociales = 0
promedioMates = 0
indicePromedio = 0 


sumaSusana = 0
sumaJuan = 0
sumaCarmen = 0
sumaPetra = 0
sumaPedro = 0
sumaFinal = 0


listaSumas = []
listaNombres = []
peorAlumno = 999999
peorAlumnoNombre = ""
mejorAlumno = 0
mejorAlumnoNombre = ""

materiaPetra = 0
materiaJuan = 60

contador = 0

for i in range(3):
    for j in range(5):
       
       
       
        
        if(j == 4):
            sumaSusana += lista[i][4]
            listaSumas.append(sumaSusana)
            listaNombres.append("susana")
        if(lista[1][j] >= puntajeSociales ):
            puntajeSociales = lista[1][j]
            indiceSociales = j
            
        if( i == 0):
             promedioMates += lista[0][j]
             
        
        if( j == 0):
            sumaJuan += lista[i][0]
            listaSumas.append(sumaJuan)
            listaNombres.append("juan")
            
        if(j == 3):
            sumaCarmen += lista[i][3]
            listaSumas.append(sumaCarmen)
            listaNombres.append("carmen")
        if(j == 2):
            sumaPetra += lista[i][2]
            listaSumas.append(sumaPetra)
            listaNombres.append("petra")
        if(j == 1):
            sumaPedro += lista[i][1] 
            listaSumas.append(sumaPedro)  
            listaNombres.append("pedro")
           
           
           
        if(j == 2):
            
            if(lista[i][j] >  materiaPetra):
                numeroMateriaPetraFinal = numeroMateriaPetra
                materiaPetra = lista[i][j]
               
            numeroMateriaPetra += 1
                
        if(j == 0):
            
            if(lista[i][j] <  materiaJuan):
                numeroMateriaJuanFinal = numeroMateriaJuan
                materiaJuan = lista[i][j]
                
            numeroMateriaJuan += 1  
               
            
        
        
for i in range(len(listaSumas)):
    
    
   
    if(listaSumas[i] > mejorAlumno):
        mejorAlumno = listaSumas[i]
        mejorAlumnoNombre = "El Mejor alumno: ",listaNombres[i] , " tiene un promedio de: " , (listaSumas[i]/3)
    if(contador >= 10):
         if(listaSumas[contador] < peorAlumno):
            peorAlumno = listaSumas[i]
            peorAlumnoNombre = "El Peor alumno: ",listaNombres[i] , " tiene un promedio de: " , (listaSumas[i]/3)
            
    contador += 1

        
    

if(sumaJuan > sumaCarmen):
    sumaFinal = sumaJuan
    indicePromedio = 0
else:
    sumaFinal = sumaCarmen  
    indicePromedio = 3      


print("El promedio de Susana es de : ", (sumaSusana / 3))
print("El mejor puntaje en sociales es de: ", listaAlumnos[indiceSociales]  , " y fue con la puntuacion de: " , puntajeSociales)
print("El promedio general de matematicas es de: " , (promedioMates/5))
print("El mejor promedio entre juan o carmen es de: " , (sumaFinal/3) , " y fue con el alumno: " , listaAlumnos[indicePromedio])
print(mejorAlumnoNombre) 
print(peorAlumnoNombre)
print("La materia de petra con mejor calificacion fue de: ",materiaPetra , " y fue en la materia: ",listaMaterias[numeroMateriaPetraFinal])
print("La materia de juan con peor calificacion fue de: ",materiaJuan , " y fue en la materia: ",listaMaterias[numeroMateriaJuanFinal])