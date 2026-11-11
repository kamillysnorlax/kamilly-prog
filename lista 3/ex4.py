# Lista para armazenar até 15 placas
placas = [""] * 15  # "" indica posição vazia

while True:
    print("\nMenu")
    print("----")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    # Cadastrar
    if opcao == 1:
        placa = input("Digite a placa do veículo: ").upper()

        posicao = -1

        # Procura uma posição vazia
        for i in range(len(placas)):
            if placas[i] == "":
                posicao = i
                break

        if posicao != -1:
            placas[posicao] = placa
            print("Placa cadastrada com sucesso!")
        else:
            print("Não há espaço disponível para cadastro.")

    # Excluir
    elif opcao == 2:
        placa_excluir = input("Digite a placa que deseja excluir: ").upper()

        encontrou = False

        for i in range(len(placas)):
            if placas[i] == placa_excluir:
                placas[i] = ""  # marca a posição como vazia
                encontrou = True
                break

        if encontrou:
            print("Placa excluída com sucesso!")
        else:
            print("Falha! Placa não encontrada.")

    # Listar
    elif opcao == 3:
        print("\nPlacas cadastradas:")

        encontrou = False

        for placa in placas:
            if placa != "":
                print(placa)
                encontrou = True

        if not encontrou:
            print("Nenhuma placa cadastrada.")

    # Sair
    elif opcao == 0:
        print("Programa encerrado.")
        break

    # Opção inválida
    else:
        print("Opção inválida!")