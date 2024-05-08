#pedir una frase desde el teclado y un numero, y desplegar esa misma frase pero colocante la longitud de cada
#linea sera de n letras (espacios se cuenta como caracter)

# usa %, list() y end=""

#iput : In publishing and graphic design, Lorem ipsum is a placeholder text commonly used to demonst
#output:

#In publish
#ing and gr
#aphic desi
#gn, Lorem
#ipsum is a
# placehold
#er text co
#mmonly use
#d to demon
#st

palabra = list(str(input("Ingrese la frase: ")))
num = int(input("Ingrese un numero: "))

for i in range(len(palabra)):

    if (i % num ) == 0:
        print()

    print(palabra[i], end="")




