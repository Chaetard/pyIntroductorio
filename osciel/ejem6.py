#Hacer un prgrama que pida desde el teclado una frase y que elimine los caracteres repetidos
#ejemplo: 
#input:
#HOOOLAAA
#output: 
#HOLA



frase1 = list(str(input("Ingrese la frase: ")))

frase2 = list()

for i in range(len(frase1)):
    
    if frase1[i].lower() != frase1[i - 1].lower():
        frase2.append(frase1[i])

for i in range(len(frase2)):
    print(frase2[i], end="")