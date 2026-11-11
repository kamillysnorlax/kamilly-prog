VERMELHO = "\033[41m"
BRANCO = "\033[47m"
AZUL = "\033[44m"
RESET = "\033[0m"

for linha in range(11):
    texto = ""

    for coluna in range(22):

        # Cruz vertical
        if coluna in [6, 9]:
            texto += BRANCO + " "
        elif coluna in [7, 8]:
            texto += AZUL + " "

        # Cruz horizontal
        elif linha in [4, 6]:
            texto += BRANCO + " "
        elif linha == 5:
            texto += AZUL + " "

        # Fundo vermelho
        else:
            texto += VERMELHO + " "

    texto += RESET
    print(texto)