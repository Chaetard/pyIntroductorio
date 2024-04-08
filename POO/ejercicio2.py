import math

ejecucion = True
elec = 0

class Triangulo:
    def area(self):
        return (self.base*self.altura)/2
    def perimetro(self):
        return self.base*3
    
class Cuadrado:
    def area(self):
        return self.lado*self.lado
    
    def perimetro(self):
        return self.lado * 4
    
class Rectangulo:
    def area(self):
        return self.base*self.altura
    
    def perimetro(self):
        return (self.base*2) + (self.altura*2)
    
class Circulo: 
    def area(self):
        return (math.pi * (self.diametro/2)) ** 2
    def perimetro(self):
        return math.pi * self.diametro
    def radio(self):
        return self.diametro / 2
    
    
while ejecucion:
    print("Triangulo -- 1")
    print("Cuadrado -- 2")
    print("Rectangulo -- 3")
    print("Circulo -- 4")
    print("Salir -- 5")
    elec = int(input("Elija la figura que desea calcular: "))
    if elec == 1:
        
        triangulo = Triangulo()
        triangulo.base = float(input("Base del triangulo: "))
        triangulo.altura = float(input("Altura del triangulo: "))
        print("Area -- 1")
        print("Perimetro -- 2")
        
        elec1 = int(input("Elija la operacion: "))
        
        if elec1 == 1:
            print("El area del triangulo es de: ",triangulo.area())
        elif elec1 == 2:
          print("El perimetro del triangulo es de: ", triangulo.perimetro())
        else:
            print("Opcion incorrecta")
        
    elif elec == 2:
        cuadrado = Cuadrado()
        cuadrado.lado = float(input("Lado del cuadrado: "))
        print("Area -- 1")
        print("Perimetro -- 2")
        
        elec1 = int(input("Elija la operacion: "))
        
        if elec1 == 1:
            print("El area del cuadrado es de: ",cuadrado.area())
        elif elec1 == 2:
          print("El perimetro del cuadrado es de: ", cuadrado.perimetro())
        else:
            print("Opcion incorrecta")
    elif elec == 3:
        rectangulo = Rectangulo()
        rectangulo.base = float(input("Base del rectangulo: "))
        rectangulo.altura = float(input("Altura del rectangulo: "))
        print("Area -- 1")
        print("Perimetro -- 2")
        
        elec1 = int(input("Elija la operacion: "))
        
        if elec1 == 1:
            print("El area del rectangulo es de: ",rectangulo.area())
        elif elec1 == 2:
          print("El perimetro del rectangulo es de: ", rectangulo.perimetro())
        else:
            print("Opcion incorrecta")
    elif elec== 4:
        circulo = Circulo()
        circulo.diametro = float(input("diametro del circulo: "))
        print("Area -- 1")
        print("Perimetro -- 2")
        print("radio -- 3")
        
        elec1 = int(input("Elija la operacion: "))
        
        if elec1 == 1:
            print("El area del circulo es de: ",circulo.area())
        elif elec1 == 2:
          print("El perimetro del circulo es de: ", circulo.perimetro())
        elif elec1 == 3:
            print("El radio del circulo es de: ", circulo.radio())
        else:
            print("Opcion incorrecta")
    elif elec == 5:
        print("Adios")
        exit()
        
    else:
        print("\n")
        print("Opcion incorrecta")
        print("\n")
        



    
    