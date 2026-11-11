class Carro:

    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor

    def pintar(self, nova_cor):
        self.cor = nova_cor

    def mostrar_cor(self):
        return self.cor


carro = Carro("Toyota", "Azul")

carro.pintar("Vermelho")

print("Nova cor do carro:", carro.mostrar_cor())