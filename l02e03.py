def main():
    num = input("Digite um inteiro: ")

    print(buzz(num))

def buzz(n):
    if int(n)%5 == 0:
        resultado = "Buzz"
    else:
        resultado = n
    
    return resultado

main()
