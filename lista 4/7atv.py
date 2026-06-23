# Lista para armazenar as notas
notas = []

while True:
    print("\nNotas")
    print("-----")
    print("1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Listar")
    print("4 - Calcular média")
    print("5 - Mostrar maior nota")
    print("6 - Mostrar menor nota")
    print("0 - Sair")

    opcao = int(input("Opção: "))

    if opcao == 1:
        nota = float(input("Digite a nota: "))
        notas.append(nota)
        print("Nota cadastrada com sucesso!")

    elif opcao == 2:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
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
            print("Erro: não há notas cadastradas")
        else:
            print("\nLista de notas:")
            for i in range(len(notas)):
                print(f"Índice {i}: {notas[i]}")

    elif opcao == 4:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            media = sum(notas) / len(notas)
            print(f"Média: {media:.2f}")

            if media >= 6:
                print("Situação: Aprovado")
            else:
                print("Situação: Reprovado")

    elif opcao == 5:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            maior = max(notas)
            print(f"Maior nota: {maior}")

    elif opcao == 6:
        if len(notas) == 0:
            print("Erro: não há notas cadastradas")
        else:
            menor = min(notas)
            print(f"Menor nota: {menor}")

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")
