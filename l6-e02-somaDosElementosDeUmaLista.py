def soma_elementos(lista):
    soma = 0
   
    for item in lista:
        soma += item

    return soma

def main():
    lista = [2, 4, 2, 2, 3, 3, 1]
    ##print(remove_repetidos(lista))
    ##print(remove_repetidos([2, 4, 2, 2, 3, 3, 1]))
    print(soma_elementos(lista))

main()


