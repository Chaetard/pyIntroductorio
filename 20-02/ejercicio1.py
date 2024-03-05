
import sys


libros = int(input("Ingrese la cantidad de libros: "))
precios = 0
unitario = 0

envio = 10 

if libros >= 2 and libros <= 5:
    for i in range(libros):
        print("Libro ", (i+1))
        
    
        unitario =  (float(input("Ingrese el precio del libro: ")))
        if unitario >= 100 and unitario <= 999:
            precios = precios + unitario  
        else:
            print("Precio Invalido")
            sys.exit()
else:
    print("cantidad no permitida")
    sys.exit()


print("El precio total es: ", (precios*.60) + (envio + (libros - 1)))
