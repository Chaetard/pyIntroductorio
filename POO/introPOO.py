class Intro:
    x = 10
    cadena  = "Hola123"
    def metodoSaluda(self):
        print("\n")
        print("Hola desde el metodoSaluda, desde la clase animal")
        print("\n")  
    def suma(self):
        self.x = Intro.x+10
        print(self.x)
        

class NoDef:
    def vacia(self):
        pass


if __name__ == "__main__":
    obj1 = Intro()
    obj1.metodoSaluda()
    obj1.suma()
    
    print("Estamos instanciando la clase NoDef")
    obj2 = NoDef()
    obj2.vacia()

    