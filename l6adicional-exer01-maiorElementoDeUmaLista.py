def maior_elemento (lista):
    maior = lista[0]

    for item in lista:
        if maior < item:
            maior = item
            
    return maior


'''
def main():
    ## lista = [2, 4, 2, 9, 3, 3, 1]
    print(maior_elemento(lista))    

main()
'''
