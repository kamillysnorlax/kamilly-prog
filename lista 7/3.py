
class Carro:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo

    def __repr__(self):
        return f"Carro: {self.modelo} | Placa: {self.placa}"


class VagaDeEstacionamento:
    def __init__(self, id_vaga):
        self.id_vaga = id_vaga
        self.carro_estacionado = None

    def ocupar_vaga(self, carro_obj):
        if self.carro_estacionado is None:
            self.carro_estacionado = carro_obj
            return True
        return False

    def liberar_vaga(self):
        self.carro_estacionado = None

    def __repr__(self):
        if self.carro_estacionado is None:
            return f"Vaga {self.id_vaga}: Livre"
        return f"Vaga {self.id_vaga}: {self.carro_estacionado}"


# Programa principal
carro = Carro("ABC-1234", "Civic")
vaga = VagaDeEstacionamento("A-101")

while True:
    print("\n--- MENU ESTACIONAMENTO ---")
    print("1 - Ver vaga")
    print("2 - Estacionar carro")
    print("3 - Liberar vaga")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        print(vaga)

    elif opcao == "2":
        placa = input("Placa do carro: ")
        modelo = input("Modelo do carro: ")
        carro = Carro(placa, modelo)

        if vaga.ocupar_vaga(carro):
            print("Carro estacionado com sucesso!")
        else:
            print("A vaga já está ocupada!")

    elif opcao == "3":
        vaga.liberar_vaga()
        print("Vaga liberada!")

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Opção inválida!")
