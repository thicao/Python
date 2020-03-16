def main():
    seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))

    dias = seg // (3600 * 24)
    segDias = seg % (3600 * 24)

    horas = segDias // 3600
    segHoras = segDias % 3600

    minutos = segHoras // 60

    segundos = segHoras % 60

        
    print ("%d dias, %d horas, %d minutos e %d segundos." %(dias,horas,minutos,segundos))

main()    
