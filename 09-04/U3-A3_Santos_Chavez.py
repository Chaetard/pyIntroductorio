class Empleado:
    def __init__(self, nombre, salario, edad):
        self._nombre = nombre
        self._salario = salario
        self._edad = edad
    
    
    
    @property
    def nombre(self):
        return self._nombre
    @property
    def salario(self):
        return self._salario

    @property
    def edad(self):
        return self._edad
    
    
    def getDatos(self):
        print("Soy empleado de nombre " , self.nombre, " tengo ", self.edad ," años y actualmente gano ", self.salario)
    
    def saludar(self):
        print("Hola, trabajo aquí", end="")
    
class Gerente(Empleado):
    def __init__(self, nombre, salario, edad, departamento):
        super().__init__(nombre, salario, edad)
        self._departamento = departamento
        
    def saludar(self):
        super().saludar()  
        print(" y soy gerente")
        
    def getDatosGerente(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años, mi salario es: {self.salario} y soy gerente del departamento de {self.departamento} ")
    
    @property
    def departamento(self):
        return self._departamento

if __name__ == "__main__":
    
    nombre = input("Nombre: ")
    salario = float(input("Salario: "))
    edad = int(input("Edad: "))
    departamento = input("Departamento: ")
    
    Persona1 = Gerente(nombre, salario, edad, departamento)
    
    Persona1.saludar()
    
    Persona1.getDatos()
    Persona1.getDatosGerente()
    
    print(Persona1.nombre)
    print(Persona1.edad)
    print(Persona1.salario)
    print(Persona1.departamento)
