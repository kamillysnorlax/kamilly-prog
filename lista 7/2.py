
class CPU:
    def __init__(self, fabricante, modelo):
        self.fabricante = fabricante
        self.modelo = modelo

    def __repr__(self):
        return f"CPU: {self.fabricante} {self.modelo}"


class Computador:
    def __init__(self, tipo, fabricante, modelo):
        self.tipo = tipo
        self.cpu = CPU(fabricante, modelo)

    def __repr__(self):
        return f"Computador: {self.tipo} | {self.cpu}"


# Programa principal
computador = Computador("Desktop", "Intel", "i7-12700K")

print(computador)
print(computador.cpu)
