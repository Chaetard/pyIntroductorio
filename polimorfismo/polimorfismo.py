class Prestamo:
    
    #Constructor
    def __init__(self, prestamo, interes, plazos):
       self._prestamo = prestamo
       self._interes = interes
       self._plazos = plazos
       
    # Getters y Setters
    @property
    def prestamo(self):
        return self._prestamo
    
    @property
    def interes(self):
        return self._interes

    @property
    def plazos(self):
        return self._plazos

    @prestamo.setter
    def prestamo(self, valor):
        self._prestamo = valor
    @interes.setter
    def interes(self, valor):
        self._interes = valor

    @plazos.setter
    def plazos(self, valor):
        self._plazos = valor
    
    def calcular_pago(self):
        pass
    
class PagosFijos(Prestamo):
    def calcular_pago(self):
       
       #FORMULA PARA SACAR EL PLAZO FIJO, BUSQUEDA POR INTERNET
        plazo_fijo = (self.prestamo * self.interes * (1 + self.interes) ** self.plazos) / ((1 + self.interes) ** self.plazos - 1)
    
       
    
        saldo_restante = self.prestamo
        
        print("{:5} {:13} {:9} {:7} {:13}".format("Plazo", "Abono Capital", "Pago Fijo", "Intereses", "Valor Final"))
        for i in range(self.plazos):
            pago_interes = saldo_restante * self.interes
            pago_capital = plazo_fijo - pago_interes
            saldo_restante -= pago_capital
            
            print("{:5d} {:13.2f} {:9.2f} {:7.2f}{:13.2f}".format(i + 1, self.prestamo - saldo_restante, plazo_fijo, pago_interes,saldo_restante), end=" ")
            print()

class PagosVariables(Prestamo):
    def calcular_pago(self):
        prestamo = self.prestamo
        interes = self.interes
        plazos = self.plazos
        
        abono_fijo = prestamo / plazos
       
       
        print("{:5} {:10} {:10} {:13} {:10} {:11} ".format("Plazo","     Saldo", "   Interes", "Abono Capital", "Pago Total", "Valor Final"))
        contador = 1
       
        while plazos >= 1:
            
            pago_total = (prestamo * interes) + abono_fijo 
            
            print("{:5} {:10.2f} {:10.2f} {:13.2f} {:10.2f} {:11.2f}".format(contador, prestamo, (prestamo * interes), abono_fijo, pago_total,prestamo-abono_fijo))
            contador = contador + 1
            prestamo -= abono_fijo
            plazos -= 1

class PagoHipoteca(Prestamo):
    def calcular_pago(self, anio):
        prestamo = self.prestamo
        interes = self.interes
        plazos = self.plazos
        
        interes = interes/12
        
        text = ""

        if anio:
            text = "Año"
        else:
            text= "Plazo"
    
        pago_mensual = (prestamo * interes) / (1 - (1 + interes)**-plazos)
       
        print("{:5} {:10} {:10} {:7}".format(text,"Pago Fijo", "Abono", "Interes")) 
        pago = 0
        while plazos >= 1:
            
            
            pago = pago_mensual - (prestamo * interes)
            monto = prestamo - pago
            prestamo  = prestamo - pago
            
            if anio and (plazos%12 == 0):
                print("{:5} {:10.2f} {:10.2f} {:7.4f}".format(plazos / 12, pago_mensual * 12, monto * 12, interes * 12))
            elif anio == False:
                print("{:5} {:10.2f} {:10.2f} {:7.4f}".format(plazos, pago_mensual, monto, interes))
                
                
            
           
            
            
            plazos -= 1



if __name__ == "__main__":
    print("Pagos Fijos")
    
    # prestamo de 12000 a 2% de interes a 12 meses o un año
    prestamoluis = PagosFijos(12000,.02,12)
    prestamoluis.calcular_pago()
    
    print()
    print("Pagos Variables")
    
    #prestamo de 1250 con un interes mensual de 1% a 25 meses
    prestamopepe = PagosVariables(1250,.01,25)
    prestamopepe.calcular_pago()
    
    
    print()
    print("Pagos Hipoteca ")
    #Aqui los plazos son en años por que es lo que encontre en creditos hipotecarios ademas basandome en el video que los mas comun es en esos tiempos
    #utilize de ejemplo la primera tabla, pagos fijos , tiempos fijos 
    
    #Prestamo de 180,000 con un interes anual de 9% a un plazo de 20 años
    prestamojuan = PagoHipoteca(180000,.09,(12*20))
    
    #al metodo de calular pago le paso un parametro si requiere que se muestre por año, false si es por cada mes y true si requiere visualizar por cada año
    prestamojuan.calcular_pago(True)

