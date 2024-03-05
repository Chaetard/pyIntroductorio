def divisible():
    valor = 7
    contador = 0
    arreglo = []

    while contador < 25:
        if (valor % 7) == 0:
            arreglo.append(valor)
            contador += 1
        valor += 1

    return arreglo


def main():
    resultado = divisible()
    print(resultado)

if __name__ == '__main__':
    main()
