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
        estudantes.append(Estudante(matricula, nome))
        print("Estudante cadastrado!")

    elif opcao == "2":
        matricula = input("Matrícula: ")
        nome = input("Nome: ")
        professores.append(Professor(matricula, nome))
        print("Professor cadastrado!")

    elif opcao == "3":
        if len(estudantes) == 0:
            print("Nenhum estudante cadastrado.")
        else:
            for estudante in estudantes:
                print(estudante)

    elif opcao == "4":
        if len(professores) == 0:
            print("Nenhum professor cadastrado.")
        else:
            for professor in professores:
                print(professor)

    elif opcao == "5":
        matricula = input("Matrícula: ")

        for estudante in estudantes:
            if estudante.matricula == matricula:
                estudante.nome = input("Novo nome: ")
                print("Estudante alterado!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == "6":
        nome = input("Nome: ")

        for estudante in estudantes:
            if estudante.nome.lower() == nome.lower():
                estudante.matricula = input("Nova matrícula: ")
                print("Estudante alterado!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == "7":
        matricula = input("Matrícula: ")

        for professor in professores:
            if professor.matricula == matricula:
                professor.nome = input("Novo nome: ")
                print("Professor alterado!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == "8":
        nome = input("Nome: ")

        for professor in professores:
            if professor.nome.lower() == nome.lower():
                professor.matricula = input("Nova matrícula: ")
                print("Professor alterado!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == "9":
        matricula = input("Matrícula: ")

        for estudante in estudantes:
            if estudante.matricula == matricula:
                estudantes.remove(estudante)
                print("Estudante excluído!")
                break
        else:
            print("Estudante não encontrado.")

    elif opcao == "10":
        matricula = input("Matrícula: ")

        for professor in professores:
            if professor.matricula == matricula:
                professores.remove(professor)
                print("Professor excluído!")
                break
        else:
            print("Professor não encontrado.")

    elif opcao == "11":
        with open("cadastro.pkl", "wb") as arquivo:
            pickle.dump(estudantes, arquivo)
            pickle.dump(professores, arquivo)

        print("Dados salvos com sucesso!")

    elif opcao == "12":
        try:
            with open("cadastro.pkl", "rb") as arquivo:
                estudantes = pickle.load(arquivo)
                professores = pickle.load(arquivo)

            print("Dados carregados com sucesso!")

        except FileNotFoundError:
            print("Arquivo de dados não encontrado.")

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")