diasTemperatura = [[25.23,32.21,29.1,32.1,27.3,32.5,28.3],["lunes","martes","miercoles","jueves","viernes","sabado","domingo"]]
promedio = 0

for row in diasTemperatura[0]:
    promedio = promedio + row

promedio/(len(diasTemperatura[0]))
masAlto = 0
masBajo = 100
posicion = 0
posicion2 = 0

print("el promedio es de:", promedio)

dias = []



for i in range (len(diasTemperatura[0])):
    dias.append(diasTemperatura[0][i] - promedio)
    print("la diferencia con el promedio del dia: ", diasTemperatura[1][i], " es de: ", dias[i])
    if diasTemperatura[0][i] > masAlto:
        masAlto = diasTemperatura[0][i]
        posicion = diasTemperatura[1][i]
        
    if diasTemperatura[0][i] < masBajo:
        masBajo = diasTemperatura[0][i]
        posicion2 = diasTemperatura[1][i]
        print(diasTemperatura[1][i])


print("la tempertatura mas alta fue de: ", masAlto , " y fue el dia:",posicion)
print("la temperatura mas baja fue de:", masBajo, " y fue el dia:", posicion2)