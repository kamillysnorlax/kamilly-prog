class Pessoa:

    def __init__(self, nome, idade, altura, peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def exibir_dados(self):
        print(self.nome, self.idade, self.altura, self.peso)

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)

    def exibir_imc(self):
        print(self.nome, "-", round(self.calcular_imc(), 2))


pessoas = []

while True:
    print("\nCadastro de Pessoas")
    print("-------------------")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        peso = float(input("Peso: "))

        pessoa = Pessoa(nome, idade, altura, peso)
        pessoas.append(pessoa)

        print("Pessoa cadastrada com sucesso!")

    elif opcao == "2":
        if len(pessoas) == 0:
            print("Nenhuma pessoa cadastrada.")
        else:
            for pessoa in pessoas:
                pessoa.exibir_dados()
                pessoa.exibir_imc()

    elif opcao == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")