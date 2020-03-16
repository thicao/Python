import math

def main():
    x1 = float(input("Coordenada x1: "))
    y1 = float(input("Coordenada y1: "))
    x2 = float(input("Coordenada x2: "))
    y2 = float(input("Coordenada y2: "))

    distancia = math.sqrt((x1 - x2) ** 2 +(y1 - y2) ** 2)

    if distancia < 10:
        print("perto")
    else:
        print("longe")
main()
