def ehPrimo(n):
    i = 1
    cont = 0

    while i <= n:
        if n % i == 0:
            cont += 1
        i += 1

    if cont == 2:
        return True
    else:
        if n == 0:
            return True
        else:
            return False




numeros = []
impares = []
pares = []
primos = []
i = 0
j = 0

while i == 0:
    i = int(input("Digite o número inicial: "))

while j == 0:
    j = int(input("Digite o número final: "))
    if j <= i:
        print("O numero final deve ser maior que o inicial.")
        j = 0
        

for x in range(i, j+1):
    numeros.append(x)

for numero in numeros:
    if numero%2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
        
    if ehPrimo(numero):
        primos.append(numero)

print("\nNo intervalo entre", i, "e", j, "temos ")
print("Números pares:", pares)
print("Números ímpares:", impares)
print("Números primos:", primos)
    
