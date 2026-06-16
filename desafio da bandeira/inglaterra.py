BRANCO = "\033[47m"
VERMELHO = "\033[41m"
RESET = "\033[0m"

for linha in range(11):
    for coluna in range(21):
        if linha == 5 or coluna == 10:
            print(VERMELHO + "  " + RESET, end="")
        else:
            print(BRANCO + "  " + RESET, end="")
    print()