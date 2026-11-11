
class ContratoDeTrabalho:
    def __init__(self, salario_bruto, percentual_impostos):
        self.salario_bruto = salario_bruto
        self.percentual_impostos = percentual_impostos

    def valor_impostos(self):
        return self.salario_bruto * self.percentual_impostos

    def __repr__(self):
        return f"Salário bruto: R$ {self.salario_bruto:.2f}"


class Funcionario:
    def __init__(self, nome, cargo, salario_bruto, percentual_impostos):
        self.nome = nome
        self.cargo = cargo
        self.contrato = ContratoDeTrabalho(
            salario_bruto, percentual_impostos
        )

    def salario_liquido(self):
        impostos = self.contrato.valor_impostos()
        return self.contrato.salario_bruto - impostos

    def __repr__(self):
        return f"Funcionário: {self.nome} | Cargo: {self.cargo}"


# Programa principal
funcionario = None

while True:
    print("\n--- MENU FUNCIONÁRIO ---")
    print("1 - Cadastrar funcionário")
    print("2 - Ver funcionário")
    print("3 - Calcular impostos")
    print("4 - Calcular salário líquido")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário bruto: R$ "))
        impostos = float(input("Percentual de impostos (ex: 0.11): "))

        funcionario = Funcionario(nome, cargo, salario, impostos)
        print("Funcionário cadastrado!")

    elif opcao == "2":
        if funcionario is not None:
            print(funcionario)
            print(funcionario.contrato)
        else:
            print("Cadastre um funcionário primeiro!")

    elif opcao == "3":
        if funcionario is not None:
            print(
                f"Impostos: R$ "
                f"{funcionario.contrato.valor_impostos():.2f}"
            )
        else:
            print("Cadastre um funcionário primeiro!")

    elif opcao == "4":
        if funcionario is not None:
            print(
                f"Salário líquido: R$ "
                f"{funcionario.salario_liquido():.2f}"
            )
        else:
            print("Cadastre um funcionário primeiro!")

    elif opcao == "5":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
