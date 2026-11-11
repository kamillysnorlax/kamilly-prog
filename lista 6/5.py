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


pessoa1 = Pessoa("Ana", 20, 1.65, 60)
pessoa2 = Pessoa("João", 25, 1.80, 80)
pessoa3 = Pessoa("Maria", 30, 1.70, 70)

pessoa1.exibir_dados()
pessoa1.exibir_imc()

pessoa2.exibir_dados()
pessoa2.exibir_imc()

pessoa3.exibir_dados()
pessoa3.exibir_imc()