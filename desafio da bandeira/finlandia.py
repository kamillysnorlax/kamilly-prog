AZUL = "\033[44m"
BRANCO = "\033[47m"
RESET = "\033[0m"

for linha in range(9):
    for coluna in range(15):
        if coluna in [4, 5] or linha in [3, 4]:
            print(AZUL + "  " + RESET, end="")
        else:
            print(BRANCO + "  " + RESET, end="")
    print()