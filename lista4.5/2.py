from datetime import datetime

# ==============================
# CADASTRO DE CONDUTORES
# ==============================

condutores = {
    "001": "Roberto Souza",
    "002": "João Graciano",
    "003": "Karine Silva",
    "004": "Pedro Luiz",
    "005": "Maria Catarina",
    "006": "Júlio Cardoso",
    "007": "Altivo Antônio",
    "008": "Jorge Gonçalves",
    "009": "Marcos Vinícius",
    "010": "Heleno Nunes",
    "011": "Mara Cristina",
    "012": "Otávio Rocha"
}

# ==============================
# CADASTRO DE CAMINHÕES
# ==============================

caminhoes = {
    "001": "Monobloco",
    "002": "Scania 112 HW",
    "003": "Volkswagen Express 4150",
    "004": "Volkswagen Express 6160",
    "005": "Volkswagen VW 17230 Worker",
    "006": "Volkswagen Express 9170",
    "007": "Iveco Daily 40s14",
    "008": "Iveco Tectro 310E28"
}

# Lista das saídas diárias
saidas = []


# ==============================
# LISTAR CAMINHÕES
# ==============================

def listar_caminhoes():
    print("\n===== CAMINHÕES =====")

    for codigo, nome in caminhoes.items():
        print(codigo, "-", nome)


# ==============================
# LISTAR CONDUTORES
# ==============================

def listar_condutores():
    print("\n===== CONDUTORES =====")

    for codigo, nome in condutores.items():
        print(codigo, "-", nome)


# ==============================
# REGISTRAR SAÍDA
# ==============================

def registrar_saida():
    print("\n===== REGISTRAR SAÍDA =====")

    codigo_caminhao = input("Código do caminhão: ")

    if codigo_caminhao not in caminhoes:
        print("Caminhão não encontrado.")
        return

    codigo_condutor = input("Código do condutor: ")

    if codigo_condutor not in condutores:
        print("Condutor não encontrado.")
        return

    data_hora = datetime.now()

    saida = {
        "caminhao": codigo_caminhao,
        "condutor": codigo_condutor,
        "data_saida": data_hora.strftime("%d/%m/%Y"),
        "hora_saida": data_hora.strftime("%H:%M:%S"),
        "data_retorno": None,
        "hora_retorno": None
    }

    saidas.append(saida)

    print("\nSaída registrada com sucesso!")
    print("Caminhão:", caminhoes[codigo_caminhao])
    print("Condutor:", condutores[codigo_condutor])
    print("Data:", saida["data_saida"])
    print("Hora:", saida["hora_saida"])


# ==============================
# REGISTRAR RETORNO
# ==============================

def registrar_retorno():
    print("\n===== REGISTRAR RETORNO =====")

    codigo_caminhao = input("Código do caminhão: ")
    codigo_condutor = input("Código do condutor: ")

    if codigo_caminhao not in caminhoes:
        print("Caminhão não encontrado.")
        return

    if codigo_condutor not in condutores:
        print("Condutor não encontrado.")
        return

    registro = None

    for saida in saidas:
        if (saida["caminhao"] == codigo_caminhao
                and saida["condutor"] == codigo_condutor
                and saida["data_retorno"] is None):
            registro = saida
            break

    if registro is None:
        print("Não existe saída pendente para esse caminhão e condutor.")
        return

    data_hora = datetime.now()

    registro["data_retorno"] = data_hora.strftime("%d/%m/%Y")
    registro["hora_retorno"] = data_hora.strftime("%H:%M:%S")

    print("\nRetorno registrado com sucesso!")
    print("Caminhão:", caminhoes[codigo_caminhao])
    print("Condutor:", condutores[codigo_condutor])
    print("Data de chegada:", registro["data_retorno"])
    print("Hora de chegada:", registro["hora_retorno"])


# ==============================
# VERIFICAR RETORNO DO CAMINHÃO
# ==============================

def verificar_retorno():
    print("\n===== VERIFICAR RETORNO =====")

    codigo_caminhao = input("Código do caminhão: ")

    if codigo_caminhao not in caminhoes:
        print("Caminhão não encontrado.")
        return

    registro = None

    for saida in reversed(saidas):
        if saida["caminhao"] == codigo_caminhao:
            registro = saida
            break

    if registro is None:
        print("Esse caminhão ainda não possui uma saída registrada.")
        return

    print("\nCaminhão:", caminhoes[codigo_caminhao])
    print("Condutor:", condutores[registro["condutor"]])

    if registro["data_retorno"] is None:
        print("STATUS: CAMINHÃO AINDA NÃO RETORNOU.")
    else:
        print("STATUS: CAMINHÃO RETORNOU.")
        print("Data de retorno:", registro["data_retorno"])
        print("Hora de retorno:", registro["hora_retorno"])


# ==============================
# LISTAR RETORNOS POR DATA
# ==============================

def listar_retornos_por_data():
    print("\n===== CAMINHÕES QUE RETORNARAM =====")

    data = input("Digite a data (DD/MM/AAAA): ")

    encontrou = False

    for saida in saidas:
        if saida["data_retorno"] == data:
            encontrou = True

            print("\nCaminhão:", saida["caminhao"],
                  "-", caminhoes[saida["caminhao"]])

            print("Condutor:", condutores[saida["condutor"]])
            print("Hora de retorno:", saida["hora_retorno"])

    if not encontrou:
        print("Nenhum caminhão retornou nessa data.")


# ==============================
# VERIFICAR TODAS AS ENTREGAS
# ==============================

def verificar_entregas_do_dia():
    print("\n===== ENTREGAS DO DIA =====")

    data = datetime.now().strftime("%d/%m/%Y")

    total = 0
    retornados = 0

    for saida in saidas:
        if saida["data_saida"] == data:
            total += 1

            if saida["data_retorno"] is not None:
                retornados += 1

    if total == 0:
        print("Nenhum caminhão saiu hoje.")
        return

    print("Data:", data)
    print("Caminhões que saíram:", total)
    print("Caminhões que retornaram:", retornados)

    if total == retornados:
        print("\nTODAS AS ENTREGAS DO DIA FORAM REALIZADAS.")
    else:
        pendentes = total - retornados
        print("\nAINDA EXISTEM ENTREGAS PENDENTES.")
        print("Caminhões que não retornaram:", pendentes)


# ==============================
# LISTAR SAÍDAS DO DIA
# ==============================

def listar_saidas():
    print("\n===== SAÍDAS REGISTRADAS =====")

    if len(saidas) == 0:
        print("Nenhuma saída registrada.")
        return

    for saida in saidas:
        print("\nCaminhão:",
              saida["caminhao"],
              "-",
              caminhoes[saida["caminhao"]])

        print("Condutor:",
              saida["condutor"],
              "-",
              condutores[saida["condutor"]])

        print("Data da saída:", saida["data_saida"])
        print("Hora da saída:", saida["hora_saida"])

        if saida["data_retorno"] is None:
            print("Retorno: AINDA NÃO RETORNOU")
        else:
            print("Data do retorno:", saida["data_retorno"])
            print("Hora do retorno:", saida["hora_retorno"])


# ==============================
# MENU PRINCIPAL
# ==============================

while True:

    print("\n====================================")
    print("     ALPHA ENTREGAS")
    print("====================================")
    print("1 - Listar caminhões")
    print("2 - Listar condutores")
    print("3 - Registrar saída")
    print("4 - Registrar retorno")
    print("5 - Verificar retorno de caminhão")
    print("6 - Listar caminhões que retornaram por data")
    print("7 - Verificar entregas do dia")
    print("8 - Listar saídas")
    print("0 - Sair")
    print("====================================")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_caminhoes()

    elif opcao == "2":
        listar_condutores()

    elif opcao == "3":
        registrar_saida()

    elif opcao == "4":
        registrar_retorno()

    elif opcao == "5":
        verificar_retorno()

    elif opcao == "6":
        listar_retornos_por_data()

    elif opcao == "7":
        verificar_entregas_do_dia()

    elif opcao == "8":
        listar_saidas()

    elif opcao == "0":
        print("Sistema encerrado.")
        break

    else:
        print("Opção inválida.")