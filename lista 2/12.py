while True:
    print("\nMenu")
    print("-------")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Divisão")
    print("4 - Multiplicação")
    print("0 - Sair")

    opcao = int(input("Digite a opção: "))

    if opcao == 0:
        print("Programa encerrado.")
        break

    elif opcao >= 1 and opcao <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            resultado = num1 + num2
            print(f"Resultado: {resultado}")

        elif opcao == 2:
            resultado = num1 - num2
            print(f"Resultado: {resultado}")

        elif opcao == 3:
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
            else:
                print("Erro: divisão por zero não é permitida!")

        elif opcao == 4:
            resultado = num1 * num2
            print(f"Resultado: {resultado}")

    else:
        print("Opção inválida! Tente novamente.")