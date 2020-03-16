def ehPrimo(n):
    i = 1
    cont = 0

    while i <= n:
        if n % i == 0:
            cont += 1
        i += 1

    if cont == 2:
        return True
    else:
        if n == 0:
            return True
        else:
            return False


def n_primos(x):
    cont = 0
    while x > 1:
        if ehPrimo(x):
            cont += 1
        x -= 1
    print(cont)




