def numero_por_extenso(numero):
    unidades = [
        "zero", "um", "dois", "três", "quatro", "cinco",
        "seis", "sete", "oito", "nove"
    ]

    especiais = {
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove"
    }

    dezenas = {
        20: "vinte",
        30: "trinta",
        40: "quarenta",
        50: "cinquenta",
        60: "sessenta",
        70: "setenta",
        80: "oitenta",
        90: "noventa"
    }

    if numero < 10:
        return unidades[numero]

    if numero < 20:
        return especiais[numero]

    if numero < 100:
        dezena = (numero // 10) * 10
        unidade = numero % 10

        if unidade == 0:
            return dezenas[dezena]

        return dezenas[dezena] + " e " + unidades[unidade]

    if numero == 100:
        return "cem"

    centenas = {
        100: "cento",
        200: "duzentos",
        300: "trezentos",
        400: "quatrocentos",
        500: "quinhentos",
        600: "seiscentos",
        700: "setecentos",
        800: "oitocentos",
        900: "novecentos"
    }

    centena = (numero // 100) * 100
    resto = numero % 100

    if resto == 0:
        return centenas[centena]

    return centenas[centena] + " e " + numero_por_extenso(resto)


def data_por_extenso(data):
    dias = {
        1: "um",
        2: "dois",
        3: "três",
        4: "quatro",
        5: "cinco",
        6: "seis",
        7: "sete",
        8: "oito",
        9: "nove",
        10: "dez",
        11: "onze",
        12: "doze",
        13: "treze",
        14: "quatorze",
        15: "quinze",
        16: "dezesseis",
        17: "dezessete",
        18: "dezoito",
        19: "dezenove",
        20: "vinte",
        21: "vinte e um",
        22: "vinte e dois",
        23: "vinte e três",
        24: "vinte e quatro",
        25: "vinte e cinco",
        26: "vinte e seis",
        27: "vinte e sete",
        28: "vinte e oito",
        29: "vinte e nove",
        30: "trinta",
        31: "trinta e um"
    }

    meses = [
        "janeiro", "fevereiro", "março", "abril",
        "maio", "junho", "julho", "agosto",
        "setembro", "outubro", "novembro", "dezembro"
    ]

    dia, mes, ano = data.split("/")

    dia = int(dia)
    mes = int(mes)
    ano = int(ano)

    if ano < 2000 or ano > 2100:
        return "Ano inválido."

    if mes < 1 or mes > 12:
        return "Mês inválido."

    return dias[dia] + " de " + meses[mes - 1] + " de " + numero_por_extenso(ano)


data = input("Digite a data (DD/MM/AAAA): ")

print(data_por_extenso(data))