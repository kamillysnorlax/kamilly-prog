
class MarcadorDePagina:
    def __init__(self, pagina_atual):
        self.pagina_atual = pagina_atual

    def __repr__(self):
        return f"Marcador na página {self.pagina_atual}"


class Livro:
    def __init__(self, titulo, total_de_paginas):
        self.titulo = titulo
        self.total_de_paginas = total_de_paginas
        self.marcador = None

    def adicionar_marcador(self, pagina):
        if self.marcador is None:
            self.marcador = MarcadorDePagina(pagina)
        else:
            self.marcador.pagina_atual = pagina

    def __repr__(self):
        return f"Livro: {self.titulo} ({self.total_de_paginas} páginas)"


# Programa principal
livro = Livro("Harry Potter", 300)

print(livro)
print("Marcador:", livro.marcador)

livro.adicionar_marcador(50)
print("Marcador:", livro.marcador)

livro.adicionar_marcador(120)
print("Marcador atualizado:", livro.marcador)
