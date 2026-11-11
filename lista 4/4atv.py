# Solicita a quantidade de cidades
quantidade = int(input("Quantas cidades deseja cadastrar? "))

# Cria a lista de cidades
cidades = []

# Lê as cidades
for i in range(quantidade):
    cidade = input(f"Digite o nome da {i+1}ª cidade: ")
    cidades.append(cidade)

# Exibe a lista cadastrada
print("\nLista de cidades cadastradas:")
for cidade in cidades:
    print(cidade)

# Solicita a cidade a ser removida
remover = input("\nDigite o nome da cidade que deseja remover: ")

# Remove a cidade, se existir
if remover in cidades:
    cidades.remove(remover)
    print(f"\nA cidade '{remover}' foi removida.")
else:
    print(f"\nA cidade '{remover}' não foi encontrada na lista.")

# Exibe a lista atualizada
print("\nLista de cidades após a remoção:")
for cidade in cidades:
    print(cidade)