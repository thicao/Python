def main():
    n = int(input("Digite um número inteiro: " ))
    digito = 0
    soma = 0
    
    if n < 0:
        print("Somente números inteiros maiores que zero.")
    else:    
        while n > 0:
            if n // 10 > 0:
                digito = n % 10
            else:
                digito = n
            soma += digito
            n = n // 10
        print(soma)


main()
