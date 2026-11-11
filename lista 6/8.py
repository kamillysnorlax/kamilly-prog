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
    print("0 - Sair")

    opcao = input("Opção: ")

    # 1 - Cadastrar estudante
    if opcao == "1":
        matricula = input("Matrícula: ")
        nome = input("Nome: ")

        estudante = Estudante(matricula, nome)
        estudantes.append(estudante)

        print("Estudante cadastrado com sucesso!")

    # 2 - Cadastrar professor
    elif opcao == "2":
        matricula = input("Matrícula: ")
        nome = input("Nome: ")

        professor = Professor(matricula, nome)
        professores.append(professor)

        print("Professor cadastrado com sucesso!")

    # 3 - Listar estudantes
    elif opcao == "3":
        print("\nEstudantes:")
        
        if len(estudantes) == 0:
            print("Nenhum estudante cadastrado.")
        else:
            for estudante in estudantes:
                print(estudante)

    # 4 - Listar professores
    elif opcao == "4":
        print("\nProfessores:")
        
        if len(professores) == 0:
            print("Nenhum professor cadastrado.")
        else:
            for professor in professores:
                print(professor)

    # 5 - Alterar estudante pela matrícula
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

    # 6 - Alterar estudante pelo nome
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

    # 7 - Alterar professor pela matrícula
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

    # 8 - Alterar professor pelo nome
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

    # 9 - Excluir estudante pela matrícula
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

    # 10 - Excluir professor pela matrícula
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

    # 0 - Sair
    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")