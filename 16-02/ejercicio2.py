raices = 0
raiz1 = 0
raiz2 = 0

a = 1
b = -3
c = 2

d = b**2 - 4*a*c  

if d >= 0:
    raiz1 = (-b - d**0.5) / (2*a)
    raiz2 = (-b + d**0.5) / (2*a)
    raices = (raiz1, raiz2)
else:
    raices = "Raíces complejas"

print("La solución es: ", raices)
