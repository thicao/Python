def main():
    num = input("Digite um inteiro: ")
    num_int = int(num)

    print(par(num_int))

def par(n):
    if n%2 == 0:
        resultado = "par"
    else:
        resultado = "ímpar"
    
    return resultado

main()
