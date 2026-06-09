# Cria uma lista vazia para armazenar as idades
idades = []

# Solicita as idades dos 6 alunos
for i in range(6):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    idades.append(idade)

# Exibe as idades maiores ou iguais a 16
print("\nIdades maiores ou iguais a 16:")

for idade in idades:
    if idade >= 16:
        print(idade)