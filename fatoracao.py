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




n = int(input("Digite um numero > 1: "))

fator = 2
mult = 0
nPrint = 0

print("Fatorando", n)
while n > 1:
    while n % fator == 0:
        mult += 1
        nPrint = n // fator
        if ehPrimo(n):
            print(n, "(primo)\t/", fator, "\t=", nPrint)
        else:
            print(n, "\t\t/", fator, "\t=", nPrint)
        n = n // fator
        
    ##if mult > 0:
      ##  print("  fator", fator, "multiplicidade", mult)
    fator += 1
    mult = 0


