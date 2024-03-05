#Qué es un lenguaje (en general, no necesariamente de programación)??
#Un lenguaje de programacion es un conjunto de caracteres, sentencias, previamente definidas que funcionan para interactuar con el lenguaje maquina y compilar 

import math

def expre1(var1, var2):
    return (var1 + var2)/2

resultado = expre1(10,12)


def expre2(var1, var2):
    return (var1 * var2) ** 0.5


def expre3(var1, var2):
    return ((1/var1) + (1/var2)) ** -1

def expre4(var1):
    return (4*math.pi*(var1 ** 2))

print(expre4(10))