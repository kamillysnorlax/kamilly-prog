def numero_extenso(n):
    unidades = [
        "zero", "um", "dois", "três", "quatro",
        "cinco", "seis", "sete", "oito", "nove"
    ]

    especiais = {
        10: "dez", 11: "onze", 12: "doze", 13: "treze",
        14: "quatorze", 15: "quinze", 16: "dezesseis",
        17: "dezessete", 18: "dezoito", 19: "dezenove"
    }

    dezenas = {
        20: "vinte", 30: "trinta", 40: "quarenta",
        50: "cinquenta", 60: "sessenta", 70: "setenta",
        80: "oitenta", 90: "noventa"
    }

    centenas = {
        100: "cento", 200: "duzentos", 300: "trezentos",
        400: "quatrocentos", 500: "quinhentos",
        600: "seiscentos", 700: "setecentos",
        800: "oitocentos", 900: "novecentos"
    }

    if n < 10:
        return unidades[n]

    if n < 20:
        return especiais[n]

    if n < 100:
        dezena = (n // 10) * 10
        resto = n % 10

        if resto == 0:
            return dezenas[dezena]

        return dezenas[dezena] + " e " + unidades[resto]

    if n == 100:
        return "cem"

    if n < 1000:
        centena = (n // 100) * 100
        resto = n % 100

        if resto == 0:
            return centenas[centena]

        return centenas[centena] + " e " + numero_extenso(resto)

    if n < 1000000:
        milhar = n // 1000
        resto = n % 1000

        if milhar == 1:
            texto = "mil"
        else:
            texto = numero_extenso(milhar) + " mil"

        if resto > 0:
            texto += " " + numero_extenso(resto)

        return texto


def valor_por_extenso(valor):
    reais = int(valor)
    centavos = round((valor - reais) * 100)

    if reais == 1:
        texto = "um real"
    else:
        texto = numero_extenso(reais) + " reais"

    if centavos == 1:
        texto += " e um centavo"
    elif centavos > 0:
        texto += " e " + numero_extenso(centavos) + " centavos"

    return texto


valor = float(input("Digite o valor: "))

print(valor_por_extenso(valor))