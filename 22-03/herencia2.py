class Poste:
    def metodo(self):
        print("Soy un poste")

class Luz:
    def metodo(self):
        print("Soy la luz")

class Farola(Poste, Luz):
    def metodo(self):
        super().metodo()
        Luz.metodo(self)
        print("Soy una farola")

if __name__ == "__main__":
    cfeluz = Farola()
    cfeluz.metodo()
    print(Farola.mro)