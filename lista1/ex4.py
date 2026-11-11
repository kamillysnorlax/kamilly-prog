print("oi")

# Solicita ao usuário a escolha do superpoder
poder = input("Escolha um superpoder (força, velocidade ou voo): ")

# Verifica a escolha e exibe o super-herói correspondente
if poder == "força":
	print("Você seria o Hulk!")
elif poder == "velocidade":
	print("Você seria o Flash!")
elif poder == "voo":
	print("Você seria o Superman!")
else:
	print("Opção inválida!")
