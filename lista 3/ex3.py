# Lista com 10 posições inicializadas com -1
codigos = [-1] * 10

while True:
    print("\nMenu")
    print("----")
    print("1 - Cadastrar")
    print("2 - Listar todos")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        codigo = int(input("Digite o código do produto: "))

        if codigo == -1:
            print("Falha! O código -1 não é permitido.")
        else:
            posicao = -1

            # Procura uma posição vaga
            for i in range(len(codigos)):
                if codigos[i] == -1:
                    posicao = i
                    break

            if posicao != -1:
                codigos[posicao] = codigo
                print("Cadastro realizado com sucesso!")
            else:
                print("Falha! Cadastro cheio.")

    elif opcao == 2:
        print("\nCódigos cadastrados:")

        encontrou = False
        for codigo in codigos:
            if codigo != -1:
                print(codigo)
                encontrou = True

        if not encontrou:
            print("Nenhum código cadastrado.")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")