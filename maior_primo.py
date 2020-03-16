def maior_primo(numero):
    while numero >= 1:
        if ehPrimo(numero):
            return numero
        numero -= 1


def ehPrimo(x):
    divisor = 1
    indPrimo = True
    while (divisor < x):
        if (x % divisor ==  0):
            if (divisor != 1) and (divisor != x):
                indPrimo = False
        divisor += 1
    return indPrimo
