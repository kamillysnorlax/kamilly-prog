# Lista para armazenar as notas
notas = []

while True:
    print("\nNotas")
    print("-----")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Calcular média")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        print("Nota cadastrada com sucesso!")

    elif opcao == 2:
        if len(notas) == 0:
            print("A lista de notas está vazia!")
        else:
            print("\nNotas cadastradas:")
            for i in range(len(notas)):
                print(f"Índice {i}: {notas[i]}")

            indice = int(input("Digite o índice da nota que deseja excluir: "))

            if 0 <= indice < len(notas):
                removida = notas.pop(indice)
                print(f"Nota {removida} removida com sucesso!")
            else:
                print("Índice inválido!")

    elif opcao == 3:
        if len(notas) == 0:
            print("A lista de notas está vazia!")
        else:
            print("\nLista de notas:")
            for i in range(len(notas)):
                print(f"Índice {i}: {notas[i]}")

    elif opcao == 4:
        if len(notas) == 0:
            print("Não há notas cadastradas para calcular a média!")
        else:
            media = sum(notas) / len(notas)

            print(f"Média: {media:.2f}")

            if media >= 6:
                print("Situação: Aprovado")
            else:
                print("Situação: Reprovado")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")