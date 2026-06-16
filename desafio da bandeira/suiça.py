VERMELHO = "\033[41m"
BRANCO = "\033[47m"
RESET = "\033[0m"

for linha in range(9):
    for coluna in range(9):
        if (linha >= 3 and linha <= 5) or (coluna >= 3 and coluna <= 5):
            print(BRANCO + "  " + RESET, end="")
        else:
            print(VERMELHO + "  " + RESET, end="")
    print()