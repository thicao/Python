def main():
    n1 = int(input("Digite o 1º inteiro: "))
    n2 = int(input("Digite o 2º inteiro: "))
    n3 = int(input("Digite o 3º inteiro: "))

    if (n1 < n2) and (n2 < n3):
        print("crescente")
    else:
        print("não está em ordem crescente")

main()
