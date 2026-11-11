
def tempo_total(horas, minutos):
    return horas * 60 + minutos


horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

total = tempo_total(horas, minutos)

print("Tempo total em minutos:", total)