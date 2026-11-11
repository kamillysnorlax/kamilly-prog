# Lista para armazenar as notas
notas = []

# Leitura das 4 notas
for i in range(4):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Cálculo da média
media = sum(notas) / len(notas)

# Exibição da média
print(f"\nMédia: {media:.2f}")

# Verificação da situação
if media >= 6:
    print("Situação: Aprovado(a)")
else:
    print("Situação: Reprovado(a)")
