import math

def main():
    xa = float(input("Digite o valor de a: "))
    xb = float(input("Digite o valor de b: "))
    xc = float(input("Digite o valor de c: "))

    calcula_raizes(xa, xb, xc)

def delta(a, b, c):
    return (b ** 2 - 4 * a * c)


def calcula_raizes(a, b, c):
    deltaLocal = delta(a, b, c)

    if deltaLocal < 0:
        print ("Esta equação não possui raízes reais.")
    else:
        raiz1 = (-b + math.sqrt(deltaLocal)) / (2 * a)    
        if deltaLocal == 0:
            print ("A única raiz é: ", raiz1)
        else:
            raiz2 = (-b - math.sqrt(deltaLocal)) / (2 * a)
            print("A primeira raiz é: ", raiz1)
            print("A segunda raiz é: ", raiz2)
