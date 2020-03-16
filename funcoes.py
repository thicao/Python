def fatorial(k):
    '''(int) -> int

    Recebe um inteiro k e retorna o valor de k!

    Pre-condicao: supoe que k eh um numero inteiro nao negativo.
    '''

    k_fat = 1
    cont = 1
    while cont < k:
        cont += 1       # o mesmo que cont = cont + 1
        k_fat *= cont   # o mesmo que k_fat = k_fat * cont

    return k_fat
	
def maximo(x, y):
	if x > y:
		return x
	else:
		return y
