def computador_escolhe_jogada(totP, maxP):
    remover = maxP
    sobra = totP - remover
    
    while (sobra % (maxP + 1) != 0):
        remover -= 1
        sobra = totP - remover

    if remover <= 0:
        remover = maxP

    return remover


def jogada_valida(nPecas, maxPecas, aRetirar):
    if aRetirar <= 0 or aRetirar > nPecas or aRetirar > maxPecas:
        return False
    else:
        return True



def usuario_escolhe_jogada(totP, maxP):
    numPecas = int(input("Quantas peças você vai tirar? "))
                   
    while not jogada_valida(totP, maxP, numPecas):
        print("Oops! Jogada inválida! Tente de novo.")
        numPecas = int(input("Quantas peças você vai tirar? "))

    return numPecas



def partida():
    pecasLeft = 0
    pecasRemover = 0
    fimJogo = False
    humanoProximoJogar = True
    ultimoAJogar = ""
    global scoreHuman
    global scoreComputer

    print(" ")
    print(" *** Início da Partida *** ")
    print(" ")
    totalPecas = int(input("Quantas peças? "))
    while totalPecas < 1:
        print("Para jogar, o total de peças deve ser maior ou igual a 1.")
        totalPecas = int(input("Quantas peças? "))

    maximoPecas = int(input("Limite de peças por jogada? "))
    while (maximoPecas < 1) or (maximoPecas > totalPecas):
        print("O limite de peças inválido.")
        maximoPecas = int(input("Limite de peças por jogada?  "))

    print(" ")
    pecasLeft = totalPecas

    ## --- Verificando quem joga primeiro
    if maximoPecas == 1:
        if ehImpar(totalPecas):
            humanoProximoJogar = False
        else:
            humanoProximoJogar = True
    else:
        if ehMultiplo (totalPecas,(maximoPecas + 1)):
            humanoProximoJogar = True
        else:
            humanoProximoJogar = False
    ## --- Fim da verificação do primeiro jogador    

    if humanoProximoJogar:
        print("Voce começa.")
    else:
        print("O Computador começa.")
    print(" ")        

    while not fimJogo:
        if humanoProximoJogar:
            pecasRemover = usuario_escolhe_jogada(pecasLeft, maximoPecas)
            if pecasRemover == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", pecasRemover, "peças.")
            humanoProximoJogar = False
            ultimoAJogar = "Você"
        else:
            pecasRemover = computador_escolhe_jogada(pecasLeft, maximoPecas)
            if pecasRemover == 1:
                print("O Computador tirou uma peça.")
            else:
                print("O computador tirou", pecasRemover, "peças.")
            humanoProximoJogar = True
            ultimoAJogar = "O Computador"
            
        print(" ")    
        pecasLeft -= pecasRemover
        if pecasLeft == 0:
            fimJogo = True
            print("Fim do jogo!", ultimoAJogar, "ganhou!")
            if humanoProximoJogar:
                scoreComputer += 1
            else:
                scoreHuman += 1
        else:
            print("Agora restam", pecasLeft, "peças no tabuleiro.")
    print(" ")

def ehMultiplo (a, b):
    if a % b == 0:
        return True
    else:
        return False

def ehImpar(a):
    if a % 2 != 0:
        return True
    else:
        return False
    
## def main():
   
    
scoreComputer = 0
scoreHuman = 0
opcao = 0
contRodada = 1


print("|-------------------------------------|")
print("| Bem-vindo ao jogo do NIM! Escolha:  |")
print("|-------------------------------------|")
print("| 1 - para jogar uma partida isolada  |")
print("| 2 - para jogar um campeonato        |")
print("|-------------------------------------|")
opcao = int(input("Sua opção: "))

while opcao != 1 and opcao != 2:
    print("Opção inválida!")
    opcao = int(input("Sua opção: "))

if opcao == 1:
    print("")
    print("Você escolheu uma partida simples")
    print("")
    print("")
    print("Rodada única começando")
    print("")
    partida()
else:
    print("")
    print("Você escolheu um campeonato")
    print("")
    print("")
    while contRodada <= 3:
        print("**** Rodada", contRodada, "****")
        print("")
        partida()
        contRodada += 1

    print("**** Final do campeonato! ****")
    print("")
    print("Placar: Você", scoreHuman, "X", scoreComputer, "Computador")
    
## main()
