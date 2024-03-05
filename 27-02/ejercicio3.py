def menu():
    print("Calculadora")
    print("teclee la opcion")
    print("1- Suma" )
    print("2- resta")
    print("3- division")
    print("4- multiplicacion")
    var = int(input())
    
    if var == 1:
        print(suma())
    elif var == 2: 
        print(resta())
    elif var == 3:
        print(division())
    elif var == 4:
        print(multi())
    else:
        print("Opcion No reconocida")
        exit()      

def suma():
    
    var1 = int(input("Valor 1: "))
    var2 = int(input("Valor 2: "))
    
    return(var1 + var2)

def resta():
    var1 = int(input("Valor 1: "))
    var2 = int(input("Valor 2: "))
    
    return(var1 - var2)
    

def division():
    var1 = int(input("Valor 1: "))
    var2 = int(input("Valor 2: "))
    
    return(var1 / var2)

def multi():
    var1 = int(input("Valor 1: "))
    var2 = int(input("Valor 2: "))
    
    return(var1 * var2)
    
    
   
def main():
    menu()   
    
if __name__ == '__main__':
    main()