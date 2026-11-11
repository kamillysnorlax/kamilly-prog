print("oi")

# Solicita a idade da pessoa
idade = int(input("Digite sua idade: "))

# Verifica a classificação indicativa permitida
if idade < 10:
	print("Você pode assistir apenas a filmes com classificação Livre.")
elif idade <= 11:
	print("Você pode assistir a filmes com classificação até 10 anos.")
elif idade <= 13:
	print("Você pode assistir a filmes com classificação até 12 anos.")
elif idade <= 15:
	print("Você pode assistir a filmes com classificação até 14 anos.")
elif idade <= 17:
	print("Você pode assistir a filmes com classificação até 16 anos.")
else:
	print("Você pode assistir a filmes com classificação até 18 anos.")