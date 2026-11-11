# Programa para registrar notas de um estudante

# Lista para armazenar as notas
notas = []

# Solicita a quantidade de notas
quantidade = int(input("Quantas notas deseja cadastrar? "))

# Leitura das notas
for i in range(quantidade):
    nota = float(input(f"Digite a {i + 1}ª nota: "))
    notas.append(nota)

# Exibição das notas cadastradas
print("\nNotas cadastradas:")

for i, nota in enumerate(notas, start=1):
    print(f"{i}ª nota: {nota}")