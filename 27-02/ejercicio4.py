def menu():
    print("Conversor de Unidades (Temperatura)")
    print("Seleccion una opcion")
    print("1- Celsius -> Fahrenheit")
    print("2- Farenheit -> Celsius")
    print("3- Kelvin -> Celsius")
    print("4- Celsius -> Kelvin")
    
    var = int(input(""))
    
    if var == 1:
        print("Fahrenheit", celFah())
    elif var == 2:
        print(fahCel())
    elif var == 3:
        print(kelCel())
    elif var == 4:
        print(celKel())
    else: 
        print("Opcion no existe")
        exit()
    
    
def celFah():
    var = int(input("Ingrese valor en Celsius: "))
    resultado = (var * 9/5) + 32
    return(resultado)

def fahCel():
    var = int(input("Ingrese valor en Fahrenheit: "))
    resultado = (var - 32) * 5/9 
    return(resultado)
    
def kelCel():
    var = int(input("Ingrese valor en Kelvin: "))
    resultado = var - 273.15 
    return(resultado)

def celKel():
    var = int(input("Ingrese valor en Celsius: "))
    resultado = var + 273.15 
    return(resultado)
    
    

def main():
    menu()   
    
if __name__ == '__main__':
    main()