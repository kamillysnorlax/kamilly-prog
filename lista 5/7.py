def desenhar_moldura(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))

    print("+" + "-" * (colunas - 2) + "+")

    for i in range(linhas - 2):
        print("|" + " " * (colunas - 2) + "|")

    if linhas > 1:
        print("+" + "-" * (colunas - 2) + "+")


linhas = int(input("Digite o número de linhas: "))
colunas = int(input("Digite o número de colunas: "))

desenhar_moldura(linhas, colunas)