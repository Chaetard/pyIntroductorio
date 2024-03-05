artiuculo1 = float(input("Ingrese el precio del Primer Articulo: "));
artiuculo2 = float(input("Ingrese el precio del Segundo Articulo: "));
artiuculo3 = float(input("Ingrese el precio del Tercer Articulo: " ));
artiuculo4 = float(input("Ingrese el precio del Cuarto Articulo: "));
artiuculo5 = float(input("Ingrese el precio del Quinto Articulo: "));

subtotal  = artiuculo1 + artiuculo2 + artiuculo3 + artiuculo4 + artiuculo5;
iva = subtotal * 0.07;

print("El subtotal es: ");  
print( format(subtotal, ">10.2f"), sep="")
print("El Impuesto es de: ");
print( format(iva, ">10.2f"), sep="")
print("El total es: ");
print( format(( subtotal + iva), ">10.2f"), sep="")

