VERDE = "\033[42m"
AMARELO = "\033[43m"
VERMELHO = "\033[41m"
RESET = "\033[0m"

for linha in range(10):
    if linha == 5:
        print(
            VERDE + " " * 10 +
            AMARELO + "    ★     " +
            VERMELHO + " " * 10 +
            RESET
        )
    else:
        print(
            VERDE + " " * 10 +
            AMARELO + " " * 10 +
            VERMELHO + " " * 10 +
            RESET
        )