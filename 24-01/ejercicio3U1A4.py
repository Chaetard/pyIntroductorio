
accionesCompradas = 2000
preciodeAccion = 40.00
comisionCompra = 0.03

accionesVendidas = 2000
preciodeVenta = 42.75
porcentajeVentaComision = 0.03

montoComprado = accionesCompradas * preciodeAccion
comisiondeCompra = montoComprado * comisionCompra

MontoTotalVenta = accionesVendidas * preciodeVenta
comiVenta = MontoTotalVenta * porcentajeVentaComision

dineroSobrante = MontoTotalVenta - comiVenta

print("Cantidad pagada por las acciones:", montoComprado)
print("Comisión pagada al corredor al comprar:", comisiondeCompra)
print("Cantidad por la que Joe vendió las acciones:", MontoTotalVenta)
print("Comisión pagada al corredor al vender:", comiVenta)
print("Cantidad de dinero que le queda a Joe:", dineroSobrante)


if dineroSobrante > 0:
    print("El Gano dinero.")
else:
    print("El perdito dinero.")
