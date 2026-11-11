# Programa para cadastrar bairros de Garopaba

# Criação da lista com o primeiro bairro adicionado manualmente
bairros = ["Centro"]

# Solicita ao usuário o cadastro de mais 5 bairros
print("Cadastro de bairros de Garopaba")

for i in range(5):
    bairro = input(f"Digite o nome do {i + 2}º bairro: ")
    bairros.append(bairro)

# Exibe todos os bairros cadastrados
print("\nLista de bairros cadastrados:")

for i, bairro in enumerate(bairros, start=1):
    print(f"{i}º bairro: {bairro}")
    