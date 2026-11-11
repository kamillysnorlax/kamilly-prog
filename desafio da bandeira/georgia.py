BRANCO = "\033[47m"
VERMELHO = "\033[41m"
RESET = "\033[0m"

for linha in range(9):
    for coluna in range(15):
        if linha == 4 or coluna == 7:
            print(VERMELHO + "  " + RESET, end="")
        elif (linha == 1 and coluna == 3) or \
             (linha == 1 and coluna == 11) or \
             (linha == 7 and coluna == 3) or \
             (linha == 7 and coluna == 11):
            print(VERMELHO + "  " + RESET, end="")
        else:
            print(BRANCO + "  " + RESET, end="")
    print()