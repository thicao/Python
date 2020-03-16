import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura
    a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que
    aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes
    utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcMedia(num_a, num_b):
    return (num_a / num_b)



def calcTamanhoMedio(lista_palavras):
    somaTamPalavras = 0
    nPalavras = 0

    for palavra in lista_palavras:
        nPalavras += 1
        somaTamPalavras += len(palavra)

    return calcMedia(somaTamPalavras, nPalavras)

    

def calcTypeToken(lista_palavras):
    nDiferentes = n_palavras_diferentes(lista_palavras)
    nPalavras = len(lista_palavras)
    
    return calcMedia(nDiferentes, nPalavras)


def calcHapaxLegomana(lista_palavras):
    nUnicas = n_palavras_unicas(lista_palavras)
    nPalavras = len(lista_palavras)
    
    return calcMedia(nUnicas, nPalavras)






def compara_assinatura(as_a, as_b):
    '''Essa funcao recebe duas assinaturas de texto e deve devolver o grau
    de similaridade nas assinaturas.'''
    ind = 0
    somaTracoLinguistico = 0
    
    while ind < 6:
        somaTracoLinguistico += abs(as_a[ind] - as_b[ind])
        ind += 1

    return (somaTracoLinguistico / 6)
    

def calcula_assinatura(texto):
    '''Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    assinatura = []
    allwords = []
    contSentencas = 0
    contCaracSentencas = 0
    contFrases = 0
    contCaracFrases = 0

    sentencas = separa_sentencas(texto)

    for sentenca in sentencas:
        #print("Sentença:", sentenca, "\n")
        contSentencas += 1
        contCaracSentencas += len(sentenca)
        frases = separa_frases(sentenca)
        #print("Frases da sentença acima:", frases, "\n")
        for frase in frases:
            contFrases += 1
            contCaracFrases += len(frase)
            #print("Frase:", frase, "\n")
            palavras = separa_palavras(frase)
            for palavra in palavras:
                allwords.append(palavra)
            
            #print("Palavras da frase acima:", palavras, "\n\n")
            
    #print("Todas as palavras:", allwords)
    #nDiferentes = n_palavras_diferentes(allwords)
    #nUnicas = n_palavras_unicas(allwords)
    #print("Palavras diferentes:", nDiferentes)
    #print("Palavras únicas:", nUnicas)
                
    assinatura.append(calcTamanhoMedio(allwords))
    #print("Tamanho médio de palavra:", calcTamanhoMedio(allwords))
    
    assinatura.append(calcTypeToken(allwords))
    #print("Relação Type-Token:", calcTypeToken(allwords))
    
    assinatura.append(calcHapaxLegomana(allwords))
    #print("Relação Hapax Legomana:", calcHapaxLegomana(allwords))

    assinatura.append(calcMedia(contCaracSentencas, contSentencas))
    #print("Tamanho médio de sentença:", calcMedia(contCaracSentencas, contSentencas))

    assinatura.append(calcMedia(contFrases, contSentencas))
    #print("Complexidade de sentença:", calcMedia(contFrases, contSentencas))

    assinatura.append(calcMedia(contCaracFrases, contFrases))
    #print("Tamanho médio de frase:", calcMedia(contCaracFrases, contFrases))

    return assinatura
    
    

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver
    o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_similaridades = []

    for texto in textos:
        lista_similaridades.append(compara_assinatura(calcula_assinatura(texto), ass_cp))

    indice = 0
    menorValor = lista_similaridades[0]
    
    for valor in lista_similaridades:
        if valor < menorValor:
            indMenorValor = indice
            menorValor = valor
        indice += 1

    return (indMenorValor + 1)
        
    

def main():

    #texto = "Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia."
    #print(texto)
    #print("Assinatura do texto:", calcula_assinatura(texto))

    ass_padrao = le_assinatura()
    #print("Assinatura de referencia:", ass_padrao)

    textos = le_textos()    
    #print("Textos:", textos)

    
    infectado = avalia_textos(textos, ass_padrao)
    #print("Infectado:", infectado)

    print("O autor do texto", infectado, "está infectado com COH-PIAH")

    

    
    

main()
