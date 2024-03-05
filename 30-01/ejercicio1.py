grados = [[12.2,11.1,11.4,10.3,9.2,20.1,21.1,22.43,23.4,22.3,22.2,23.23,12.2,11.1,11.4,10.3,9.2,20.1,21.1,22.43,23.4,22.3,22.2,23.23, ], ["0 am", "1 am", "2 am", "3 am", "4 am", "5 am", "6 am", "7 am", "8 am", "9 am", "10 am", "11 am", "12 pm", "1 pm", "2 pm", "3 pm", "4 pm", "5 pm", "6 pm", "7 pm", "8 pm", "9 pm", "10 pm", "11 pm"]]


masAlto = 0
masBajo = 100
posicion = 0
posicion2 = 100

mediaSuma = 0

for row in grados[0]:
    if row > masAlto:
        masAlto = row
        posicion = grados[0].index(row)
    if row < masBajo:
        masBajo = row
        posicion2 = grados[0].index(row)
    
    mediaSuma = mediaSuma + row
     
        

print("La temperatura mas alta fue de: ", masAlto, " a las: ", grados[1][posicion])
print("La temperatura mas baja fue de: ", masBajo, " a las: ", grados[1][posicion2])


print("y la media fue de ", mediaSuma/(len(grados[0])))