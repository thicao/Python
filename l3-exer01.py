def main():
    n = int(input("Digite o valor de n: " ))

    print(fatorial(n))

def fatorial(num):
    fatorial = 1

    if num <= 1:
        if num < 0:
            resp = "Fatorial apenas de números inteiros não negativos"
        else:
            resp =  "1"
    else:
        while num >= 1:
            fatorial = fatorial * num
            num -= 1
        resp = str(fatorial)
    return resp
main()
