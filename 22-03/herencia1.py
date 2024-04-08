class Persona:
    def metodo(self):
        print("este es un metodo de la clase persona")


class Estudiante(Persona):
    
    def metodo(self):
        super().metodo()
        print("Este es un metodo de la clase estudiante")     
        
class Profesor(Persona):
    
    def metodo(self):
        super().metodo()
        print("Este es un metodo de la clase profesor")
        
class EstudianteDoctorado(Estudiante):
   
    def metodo(self):
        super().metodo()
        print("Este es un metodo de la clase EstudianteDoctorado")

class ProfesorAyudante(EstudianteDoctorado, Profesor):
   
    def metodo(self):
        super().metodo()
        print("Este es un metodo de la clase ProfesorAyudante")
        
if __name__ == "__main__":
    Joaquin = ProfesorAyudante()
    
    Joaquin.metodo()
    
          
        

