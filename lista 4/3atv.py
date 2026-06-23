# Criando uma lista vazia
notas = []

# Lendo 3 notas
for i in range(3):
    nota = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota)

# Exibição com while
print("\nExibição com while:")
i = 0
while i < len(notas):
    print(f"Nota: {notas[i]}")
    i += 1

# Exibição com for
print("\nExibição com for:")
for nota in notas:
    print(f"Nota: {nota}")