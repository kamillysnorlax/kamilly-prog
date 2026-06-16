from deep_translator import GoogleTranslator

idiomas = {
    "1": "es",
    "2": "it",
    "3": "fr",
    "4": "en"
}

while True:
    print("\n=== TRADUTOR ===")
    print("Digite uma frase em português (ou 'sair' para encerrar):")
    texto = input("> ")

    if texto.lower() == "sair":
        print("Programa encerrado.")
        break

    print("\nEscolha o idioma:")
    print("1 - Espanhol")
    print("2 - Italiano")
    print("3 - Francês")
    print("4 - Inglês")
    print("0 - Sair")

    opcao = input("Número: ")

    if opcao == "0":
        print("Programa encerrado.")
        break

    if opcao not in idiomas:
        print("Opção inválida!")
        continue

    idioma = idiomas[opcao]

    traducao = GoogleTranslator(
        source="pt",
        target=idioma
    ).translate(texto)

    print("\nTRADUÇÃO:")
    print(traducao)