AZUL = "\033[44m"
BRANCO = "\033[47m"
VERMELHO = "\033[41m"
RESET = "\033[0m"

# Parte superior
for i in range(3):
    if i == 1:
        print(
            AZUL + "    ★    " +
            BRANCO + " " * 20 +
            RESET
        )
    else:
        print(
            AZUL + " " * 9 +
            BRANCO + " " * 20 +
            RESET
        )

# Parte inferior
for i in range(4):
    print(VERMELHO + " " * 29 + RESET)