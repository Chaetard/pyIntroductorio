class Celular:
    
    def marcar(self):
        print("Estoy marcando desde mi" , self.marca)
        print("\n")
        
    def mensajear(self):
        print("Estoy Mensajeando")
        print("\n")
        
    def contestar(self):
        print("Estoy Contestando")
        print("\n")
        
    def ponerSaldo(self):
        print("Estoy Poniendo Saldo")
        print("\n")
        
    def atributos(self):
        print("Atributos")
        print(self.marca)
        print(self.modelo)
        print(self.camara)
        print(self.internet)
        print(self.bluetooth)
        print("\n")
        
if __name__ == "__main__":
    motorola = Celular()
    motorola.marca = "Motorola"
    motorola.modelo = "KSK1000"
    motorola.camara = True
    motorola.internet = "Y"
    motorola.bluetooth = False
        
    motorola.marcar()
    motorola.mensajear()
    motorola.contestar()
    motorola.ponerSaldo()
    motorola.atributos()
    
    
    huawei = Celular()
    huawei.marca = "huawei"
    huawei.modelo = "KSK1000"
    huawei.camara = True
    huawei.internet = "Y"
    huawei.bluetooth = False
        
    huawei.marcar()
    huawei.mensajear()
    huawei.contestar()
    huawei.ponerSaldo()
    huawei.atributos()
    
    
    sony = Celular()
    sony.marca = "sony"
    sony.modelo = "KSK1000"
    sony.camara = True
    sony.internet = "Y"
    sony.bluetooth = False
        
    sony.marcar()
    sony.mensajear()
    sony.contestar()
    sony.ponerSaldo()
    sony.atributos()