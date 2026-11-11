print("oi")

# Solicita a temperatura do dia
temperatura = float(input("Digite a temperatura do dia (°C): "))

# Verifica a faixa de temperatura
if temperatura < -10:
	print("Está muito frio! Use roupas quentes.")
elif temperatura <= 20:
	print("Frio. Vista-se bem!")
elif temperatura <= 25:
	print("Temperatura agradável.")
elif temperatura <= 30:
	print("Está ficando quente!")
else:
	print("Está muito quente! Fique hidratado.")
