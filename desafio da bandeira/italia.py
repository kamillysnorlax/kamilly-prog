VERDE = "\033[42m"
BRANCO = "\033[47m"
VERMELHO = "\033[41m"
RESET = "\033[0m"

for i in range(10):
    print(
        VERDE + " " * 10 +
        BRANCO + " " * 10 +
        VERMELHO + " " * 10 +
        RESET
    )