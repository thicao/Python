
def main():
    n = int(input("Digite um número (0 para terminar): "))
    lista = []
    while n != 0:
        lista.append(n)
        n = int(input("Digite um número (0 para terminar): "))        

    for x in range(len(lista)-1, -1, -1):
        print (lista[x])
    


main()        
