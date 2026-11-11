print("oi")

# Solicita as escolhas dos jogadores
jogador1 = input("Jogador 1 (pedra, papel ou tesoura): ")
jogador2 = input("Jogador 2 (pedra, papel ou tesoura): ")

# Verifica o resultado
if jogador1 == jogador2:
	print("Empate!")
elif (jogador1 == "pedra" and jogador2 == "tesoura") or \
 	(jogador1 == "tesoura" and jogador2 == "papel") or \
 	(jogador1 == "papel" and jogador2 == "pedra"):
	print("Jogador 1 venceu!")
else:
	print("Jogador 2 venceu!")
