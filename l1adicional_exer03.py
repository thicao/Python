def main():
    n1 = input("Digite um número inteiro: ")
    n2 = int(n1)

    dezena = n2 % 100

    ndezena = dezena // 10

    print("O dígito das dezenas é", ndezena)
main()
