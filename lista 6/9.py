import pickle


class Estudante:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def __str__(self):
        return f"Matrícula: {self.matricula} | Nome: {self.nome}"


class Professor:
    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def __str__(self):
        return f"Matrícula: {self.matricula} | Nome: {self.nome}"


estudantes = []
professores = []


while True:
    print("\nSistema de Cadastro")
    print("-------------------")
    print("1 - Cadastrar estudante")
    print("2 - Cadastrar professor")
    print("3 - Listar estudantes")
    print("4 - Listar professores")
    print("5 - Alterar estudante pela matrícula")
    print("6 - Alterar estudante pelo nome")
    print("7 - Alterar professor pela matrícula")
    print("8 - Alterar professor pelo nome")
    print("9 - Excluir estudante pela matrícula")
    print("10 - Excluir professor pela matrícula")
    print("11 - Salvar dados")
    print("12 - Carregar dados")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        matricula = input("Matrícula: ")
        nome = input("Nome: ")

        estudante = Estudante(matricula, nome)
        estudantes.append(estudante)

        print("Estudante cadastrado com sucesso!")

    elif opcao == "2":
        matricula = input("Matrícula: ")
        nome = input("Nome: ")

        professor = Professor(matricula, nome)
        professores.append(professor)

        print("Professor cadastrado com sucesso!")

    elif opcao == "3":
        print("\nEstudantes:")

        if len(estudantes) == 0:
            print("Nenhum estudante cadastrado.")
        else:
            for estudante in estudantes:
                print(estudante)

    elif opcao == "4":
        print("\nProfessores:")

        if len(professores) == 0:
            print("Nenhum professor cadastrado.")
        else:
            for professor in professores:
                print(professor)

    elif opcao == "5":
        matricula = input("Digite a matrícula do estudante: ")

        encontrado = False

        for estudante in estudantes:
            if estudante.matricula == matricula:
                estudante.nome = input("Novo nome: ")
                print("Estudante alterado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Estudante não encontrado.")

    elif opcao == "6":
        nome = input("Digite o nome do estudante: ")

        encontrado = False

        for estudante in estudantes:
            if estudante.nome.lower() == nome.lower():
                estudante.matricula = input("Nova matrícula: ")
                print("Estudante alterado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Estudante não encontrado.")

    elif opcao == "7":
        matricula = input("Digite a matrícula do professor: ")

        encontrado = False

        for professor in professores:
            if professor.matricula == matricula:
                professor.nome = input("Novo nome: ")
                print("Professor alterado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Professor não encontrado.")

    elif opcao == "8":
        nome = input("Digite o nome do professor: ")

        encontrado = False

        for professor in professores:
            if professor.nome.lower() == nome.lower():
                professor.matricula = input("Nova matrícula: ")
                print("Professor alterado com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Professor não encontrado.")

    elif opcao == "9":
        matricula = input("Digite a matrícula do estudante: ")

        encontrado = False

        for estudante in estudantes:
            if estudante.matricula == matricula:
                estudantes.remove(estudante)
                print("Estudante excluído com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Estudante não encontrado.")

    elif opcao == "10":
        matricula = input("Digite a matrícula do professor: ")

        encontrado = False

        for professor in professores:
            if professor.matricula == matricula:
                professores.remove(professor)
                print("Professor excluído com sucesso!")
                encontrado = True
                break

        if not encontrado:
            print("Professor não encontrado.")

    # 11 - Salvar dados
    elif opcao == "11":
        dados = {
            "estudantes": estudantes,
            "professores": professores
        }

        with open("cadastro.pkl", "wb") as arquivo:
            pickle.dump(dados, arquivo)

        print("Dados salvos com sucesso!")

    # 12 - Carregar dados
    elif opcao == "12":
        try:
            with open("cadastro.pkl", "rb") as arquivo:
                dados = pickle.load(arquivo)

            estudantes = dados["estudantes"]
            professores = dados["professores"]

            print("Dados carregados com sucesso!")

        except FileNotFoundError:
            print("Nenhum arquivo de dados encontrado.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")