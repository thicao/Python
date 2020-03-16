def main():
    n = int(input("Digite o valor de n: " ))
    impares = 1

    if n <= 0:
        print("Somente números inteiros maiores que zero.")
    else:    
        while n > 0:
            if impares % 2 != 0:
                print(impares)
            impares += 2
            n -= 1


main()
