class Barco: 
    def metodo(self):
        print("Soy un barco")

class Avion:
    def metodo(self):
        print("soy un avion")
        
class Hidroavion(Barco, Avion):
    def metodo(self):
        super().metodo()
        Avion.metodo(self)
        print("Soy la combinacion de avion y barco, soy un hridroavion")
        
if __name__ == "__main__":
    boeingOceano = Hidroavion()
    
    boeingOceano.metodo()