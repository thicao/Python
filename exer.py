def main():
    seq = []   # inicia com uma lista vazia
    i = 1
    n = int(input("Digite um número n: "))
    
    while i <= n:
        novo_elemento = i
        seq.append( novo_elemento )
        i = i + 1
    print("Inteiros: ", seq)

main()
