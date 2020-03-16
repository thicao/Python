def remove_repetidos(lista):
    lista.sort()
    lis = []
    ult = lista[0]
    
    for item in lista:
        if item != ult:
            lis.append(ult)
        ult = item

    if lis[-1] != ult:
        lis.append(ult)
    
    return lis

''''def main():
    lista = [2, 4, 2, 2, 3, 3, 1]
    print(remove_repetidos(lista))
    print(remove_repetidos([2, 4, 2, 2, 3, 3, 1]))

main()'''
