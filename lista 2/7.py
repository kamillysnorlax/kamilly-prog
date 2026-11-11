# Solicita a quantidade de notas
quantidade = int(input("Digite a quantidade de notas: "))

soma = 0

# Lê as notas e soma os valores
for i in range(quantidade):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma += nota

# Calcula a média
media = soma / quantidade

# Exibe a média
print(f"\nMédia final: {media:.2f}")

# Verifica se foi aprovado ou reprovado
if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")