class Livro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        return f"{self.titulo} foi escrito por {self.autor}."


livro = Livro("O Conto de Aragorn e Arwen", "J. R. R. Tolkien")

print(livro.descricao())