# Listas para armazenar os dados
codigos = []
nomes = []
idades = []
alturas = []
pesos = []

codigo_atual = 1

while True:
    print("\nMenu")
    print("----")
    print("1 - Cadastrar")
    print("2 - Excluir por nome")
    print("3 - Alterar")
    print("4 - Listar")
    print("5 - Excluir por código")
    print("6 - Pesquisar por nome")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    # Cadastrar
    if opcao == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura (m): "))
        peso = float(input("Peso (kg): "))

        codigos.append(codigo_atual)
        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)

        print(f"Cadastro realizado com sucesso! Código: {codigo_atual}")
        codigo_atual += 1

    # Excluir por nome
    elif opcao == 2:
        nome = input("Digite o nome da pessoa a excluir: ")

        if nome in nomes:
            indice = nomes.index(nome)

            codigos.pop(indice)
            nomes.pop(indice)
            idades.pop(indice)
            alturas.pop(indice)
            pesos.pop(indice)

            print("Cadastro excluído com sucesso!")
        else:
            print("Pessoa não encontrada!")

    # Alterar
    elif opcao == 3:
        nome = input("Digite o nome da pessoa a alterar: ")

        if nome in nomes:
            indice = nomes.index(nome)

            idades[indice] = int(input("Nova idade: "))
            alturas[indice] = float(input("Nova altura (m): "))
            pesos[indice] = float(input("Novo peso (kg): "))

            print("Cadastro alterado com sucesso!")
        else:
            print("Pessoa não encontrada!")

    # Listar
    elif opcao == 4:
        if len(nomes) == 0:
            print("Nenhum cadastro encontrado.")
        else:
            print("\nPessoas cadastradas:")
            for i in range(len(nomes)):
                print("--------------------")
                print("Código:", codigos[i])
                print("Nome:", nomes[i])
                print("Idade:", idades[i], "anos")
                print("Altura:", alturas[i], "m")
                print("Peso:", pesos[i], "kg")

    # Excluir por código
    elif opcao == 5:
        codigo = int(input("Digite o código da pessoa: "))

        if codigo in codigos:
            indice = codigos.index(codigo)

            codigos.pop(indice)
            nomes.pop(indice)
            idades.pop(indice)
            alturas.pop(indice)
            pesos.pop(indice)

            print("Cadastro excluído com sucesso!")
        else:
            print("Código não encontrado!")

    # Pesquisar por nome
    elif opcao == 6:
        nome = input("Digite o nome da pessoa: ")

        if nome in nomes:
            indice = nomes.index(nome)

            print("\nDados encontrados:")
            print("Código:", codigos[indice])
            print("Nome:", nomes[indice])
            print("Idade:", idades[indice], "anos")
            print("Altura:", alturas[indice], "m")
            print("Peso:", pesos[indice], "kg")
        else:
            print("Pessoa não encontrada!")

    # Sair
    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")