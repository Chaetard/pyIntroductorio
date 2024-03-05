fecha = int(input("Ingrese la fecha en forma de aaaammdd: "))

anio = fecha // 10000
residuo = fecha % 10000
mes = residuo // 100
dia = residuo % 100

print("Año:", anio) 
print("Mes:", mes)
print("Día:", dia)