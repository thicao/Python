def main():
    num = input("Digite um inteiro: ")
    num_int = int(num)
    soma = []
    soma_int = 0

    while num_int != 0:
        soma.append(num)
        soma_int +=  num_int
        num = input("Digite um inteiro: ")
        num_int = int(num)

    print("A soma dos numeros ", soma[:], "é", soma_int)
    
    print(soma_int, par(soma_int), "e", primo(soma_int))

def par(n):
    if n%2 == 0:
        resultado = "é par"
    else:
        resultado = "é ímpar"
    
    return resultado

def primo(n):
    x = 1
    cont = 0
    
    while x <= n:
        if n%x == 0:
            cont += 1
        x+=1
        
    if n != 1:
        if cont == 2:
            resp = "é primo"
        else:
            resp = "não é primo"
    else:
        resp = "é primo"

    return resp

main()
