def main():
    num = input("Digite um inteiro: ")

    print(fizz(num))

def fizz(n):
    if int(n)%3 == 0:
        resultado = "Fizz"
    else:
        resultado = n
    
    return resultado

main()
