professores = {
    "001": "Prof Thiago Paes",
    "002": "Prof Schalata",
    "003": "Prof Ignácio",
    "004": "Prof Ryan",
    "005": "Prof André",
    "006": "Profª Fabiana",
    "007": "Prof Alberto",
    "008": "Prof Juliano",
    "009": "Prof Thiago Waltrik",
    "010": "Prof João Eduardo"
}

laboratorios = [
    "Lab102",
    "Lab103",
    "Lab104",
    "Lab105",
    "Lab106",
    "Lab107"
]

acessos = {
    "Lab102": ["003", "001", "004", "005", "006"],
    "Lab103": ["007"],
    "Lab104": ["004", "008", "002", "005"],
    "Lab105": ["003", "007", "009", "001"],
    "Lab106": ["002", "003", "009", "001"],
    "Lab107": ["005", "002", "009", "001", "010"]
}


# ==============================
# PROFESSORES
# ==============================

def adicionar_professor():
    codigo = input("Código do professor: ")

    if codigo in professores:
        print("Erro: código já cadastrado.")
        return

    nome = input("Nome do professor: ")

    professores[codigo] = nome
    print("Professor cadastrado com sucesso!")


def alterar_professor():
    codigo = input("Código do professor: ")

    if codigo not in professores:
        print("Erro: professor não encontrado.")
        return

    novo_nome = input("Novo nome: ")
    professores[codigo] = novo_nome

    print("Professor alterado com sucesso!")


def excluir_professor():
    codigo = input("Código do professor: ")

    if codigo not in professores:
        print("Erro: professor não encontrado.")
        return

    # Remove o professor dos acessos
    for laboratorio in laboratorios:
        if codigo in acessos[laboratorio]:
            acessos[laboratorio].remove(codigo)

    del professores[codigo]

    print("Professor excluído com sucesso!")


def listar_professores():
    print("\n===== PROFESSORES =====")

    if not professores:
        print("Nenhum professor cadastrado.")
        return

    for codigo, nome in professores.items():
        print(codigo, "-", nome)


# ==============================
# ACESSOS
# ==============================

def adicionar_acesso():
    print("\nLaboratórios disponíveis:")

    for laboratorio in laboratorios:
        print("-", laboratorio)

    laboratorio = input("Laboratório: ")

    if laboratorio not in laboratorios:
        print("Erro: laboratório inválido.")
        return

    codigo = input("Código do professor: ")

    if codigo not in professores:
        print("Erro: professor não encontrado.")
        return

    if codigo in acessos[laboratorio]:
        print("Esse professor já possui acesso a esse laboratório.")
        return

    acessos[laboratorio].append(codigo)

    print("Acesso cadastrado com sucesso!")


def alterar_acesso():
    codigo = input("Código do professor: ")

    if codigo not in professores:
        print("Erro: professor não encontrado.")
        return

    print("\nLaboratórios atuais do professor:")

    encontrou = False

    for laboratorio in laboratorios:
        if codigo in acessos[laboratorio]:
            print("-", laboratorio)
            encontrou = True

    if not encontrou:
        print("O professor não possui acessos.")
        return

    laboratorio_atual = input("Laboratório que deseja alterar: ")

    if laboratorio_atual not in laboratorios:
        print("Erro: laboratório inválido.")
        return

    if codigo not in acessos[laboratorio_atual]:
        print("O professor não possui acesso a esse laboratório.")
        return

    print("\nLaboratórios disponíveis:")
    for laboratorio in laboratorios:
        print("-", laboratorio)

    novo_laboratorio = input("Novo laboratório: ")

    if novo_laboratorio not in laboratorios:
        print("Erro: laboratório inválido.")
        return

    if codigo in acessos[novo_laboratorio]:
        print("O professor já possui acesso ao novo laboratório.")
        return

    acessos[laboratorio_atual].remove(codigo)
    acessos[novo_laboratorio].append(codigo)

    print("Acesso alterado com sucesso!")


def excluir_acesso():
    laboratorio = input("Laboratório: ")

    if laboratorio not in laboratorios:
        print("Erro: laboratório inválido.")
        return

    codigo = input("Código do professor: ")

    if codigo not in professores:
        print("Erro: professor não encontrado.")
        return

    if codigo not in acessos[laboratorio]:
        print("Esse professor não possui acesso a esse laboratório.")
        return

    acessos[laboratorio].remove(codigo)

    print("Acesso excluído com sucesso!")


def listar_acessos():
    print("\n===== ACESSOS =====")

    for laboratorio in laboratorios:
        print("\n", laboratorio)

        if not acessos[laboratorio]:
            print("  Nenhum professor autorizado.")
        else:
            for codigo in acessos[laboratorio]:
                print(" ", codigo, "-", professores[codigo])


# ==============================
# TESTE DE ACESSO
# ==============================

def testar_acesso():
    print("\n===== TESTE DE ACESSO =====")

    laboratorio = input("Laboratório: ")
    codigo = input("Código do professor: ")

    if laboratorio not in laboratorios:
        print("Laboratório inválido.")
        return

    if codigo not in professores:
        print("Professor não encontrado.")
        return

    print("\nProfessor:", professores[codigo])
    print("Laboratório:", laboratorio)

    if codigo in acessos[laboratorio]:
        print(">>> ACESSO PERMITIDO <<<")
    else:
        print(">>> ACESSO NEGADO <<<")


# ==============================
# MENU PROFESSORES
# ==============================

def menu_professores():
    while True:
        print("\n===== CADASTRO DE PROFESSORES =====")
        print("1 - Adicionar")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_professor()

        elif opcao == "2":
            alterar_professor()

        elif opcao == "3":
            excluir_professor()

        elif opcao == "4":
            listar_professores()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


# ==============================
# MENU ACESSOS
# ==============================

def menu_acessos():
    while True:
        print("\n===== CADASTRO DE ACESSOS =====")
        print("1 - Adicionar acesso")
        print("2 - Alterar acesso")
        print("3 - Excluir acesso")
        print("4 - Listar acessos")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_acesso()

        elif opcao == "2":
            alterar_acesso()

        elif opcao == "3":
            excluir_acesso()

        elif opcao == "4":
            listar_acessos()

        elif opcao == "0":
            break

        else:
            print("Opção inválida.")


# ==============================
# MENU PRINCIPAL
# ==============================

while True:
    print("\n==============================")
    print(" SISTEMA DE ACESSO - LABORATÓRIOS")
    print("==============================")
    print("1 - Cadastro de professores")
    print("2 - Cadastro de acessos")
    print("3 - Testar acesso")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        menu_professores()

    elif opcao == "2":
        menu_acessos()

    elif opcao == "3":
        testar_acesso()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")