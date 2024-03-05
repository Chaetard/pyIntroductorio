millasHora = 70;

primerTiempo = 6;
segundoTiempo = 10;
tercerTiempo = 15;

distancia1 = millasHora * primerTiempo;
distancia2 = millasHora * segundoTiempo;
distancia3 = millasHora * tercerTiempo;

print("Las millas recorridas en 6 horas son de: ");
print( format(distancia1, ">10.2f"), sep="")
print("Las millas recorridas en 10 horas son de: ");
print( format(distancia2, ">10.2f"), sep="")
print("Las millas recorridas en 15 horas son de: ");
print( format(distancia3, ">10.2f"), sep="")
