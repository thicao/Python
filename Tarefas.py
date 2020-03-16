def main():
#    num = int(input("Digite um inteiro: "))
#    fatorial = 1
#    num_original = num

#    while num != 0:
#        fatorial = fatorial * num
#        num = num - 1

#    print("O fatorial de %d é %d" %(num_original, fatorial))

    num=int(input("Quantos números serão digitados? "))
    i = 0
    pares = 0
    impares = 0
    
    while num <= 0:
        num=int(input("Favor digitar um numero inteiro maior que zero: "))

    print("Serão apurados quantos dos próximos %d números digitados são pares ou ímpares" %(num))

    while num > 0:
        i = int(input("Digite um número:"))
        if i % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1
        num = num - 1
     
    print("Total de números pares digitados:", pares)
    print("Total de números ímpares digitados:", impares)
    print(" ")


    nAlunos = int(input("Digite a quantidade de alunos: "))

    while nAlunos <= 0:
        nAlunos=int(input("Favor digitar uma quantidade de alunos válida: "))
    
    i = 1
    aprovados = 0
    reprovados = 0
    recupera = 0
    muitoBom = 0
    
    while i <= nAlunos:
        nota=float(input("Digite a nota do aluno %d: " %i))
        while nota < 0:
            nota=float(input("Digite uma nota válida para o aluno %d: " %i))
        i = i + 1
            
        if nota >= 5:
            aprovados = aprovados + 1
            if nota > 8:
                muitoBom = muitoBom + 1
        else:
            if nota >= 3:
                recupera = recupera + 1
            else:
                reprovados = reprovados + 1

    print("")
    print("Total de alunos reprovados:", reprovados)
    print("Total de alunos em recuperação:", recupera)    
    print("Total de alunos aprovados:", aprovados)
    print("Total de alunos desempenho muito bom:", muitoBom)
         
                  
main()
