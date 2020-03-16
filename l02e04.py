def main():
    num = input("Digite um inteiro: ")

    r1 = fizz(num)
    r2 = buzz(num)

    if r1 == "Fizz":
        if r2 == "Buzz":
            print("FizzBuzz")
        else:
            print(r2)
    else:
        print(r1)



def buzz(n):
    if int(n)%5 == 0:
        resultado = "Buzz"
    else:
        resultado = n
    
    return resultado


def fizz(n):
    if int(n)%3 == 0:
        resultado = "Fizz"
    else:
        resultado = n
    
    return resultado

main()
