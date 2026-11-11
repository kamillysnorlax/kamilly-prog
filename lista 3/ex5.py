# Listas para armazenar os dados
# Listas para armazenar os dados das pessoas
nomes = []
idades = []
alturas = []
pesos = []

while True:
    print("\nMenu")
    print("----")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Alterar")
    print("4 - Listar")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    # Cadastrar
    if opcao == 1:
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura (m): "))
        peso = float(input("Peso (kg): "))

        nomes.append(nome)
        idades.append(idade)
        alturas.append(altura)
        pesos.append(peso)

        print("Cadastro realizado com sucesso!")

    # Excluir
    elif opcao == 2:
        nome = input("Digite o nome da pessoa a excluir: ")

        if nome in nomes:
            indice = nomes.index(nome)

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

            print("Digite os novos dados:")
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
                print("Nome:", nomes[i])
                print("Idade:", idades[i], "anos")
                print("Altura:", alturas[i], "m")
                print("Peso:", pesos[i], "kg")

    # Sair
    elif opcao == 0:
        print("Programa encerrado.")
        break

    # Opção inválida
    else:
        print("Opção inválida!")