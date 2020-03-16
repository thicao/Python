def main():
    F = float(input("Qual a temperatura em Fahrenheit? "))
    C = float(fahrenheitToCelsius(F))

    print ("%dºF = %dºC" %(F,C))

def fahrenheitToCelsius(f):
    c = float((f - 32) * 5 / 9)
    return c

main()    
