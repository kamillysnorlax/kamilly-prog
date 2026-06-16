PRETO = "\033[40m"
VERMELHO = "\033[41m"
AMARELO = "\033[43m"
RESET = "\033[0m"

for i in range(3):
    print(PRETO + " " * 30 + RESET)

for i in range(3):
    print(VERMELHO + " " * 30 + RESET)

for i in range(3):
    print(AMARELO + " " * 30 + RESET)