class ContaBancaria:

    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def mostrar_saldo(self):
        return self.saldo


conta = ContaBancaria("Maria", 1000)

conta.depositar(500)
conta.depositar(200)

conta.sacar(300)

print("Saldo atual:", conta.mostrar_saldo())