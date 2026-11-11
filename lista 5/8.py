def converter_hora(hora):
    horas, minutos = hora.split(":")
    horas = int(horas)

    if horas < 12:
        periodo = "A"
    else:
        periodo = "P"

    if horas == 0:
        horas = 12
    elif horas > 12:
        horas -= 12

    return horas, minutos, periodo


def imprimir_hora(horas, minutos, periodo):
    if periodo == "A":
        print(f"{horas}:{minutos} A.M.")
    else:
        print(f"{horas}:{minutos} P.M.")


while True:
    hora = input("Digite a hora (HH:MM): ")

    horas, minutos, periodo = converter_hora(hora)

    imprimir_hora(horas, minutos, periodo)

    continuar = input("Deseja converter outra hora? (s/n): ")

    if continuar.lower() != "s":
        break