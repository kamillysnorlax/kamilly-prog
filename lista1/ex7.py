print("oi")

# Solicita o dia e o mês de nascimento
dia = int(input("Digite o dia do nascimento: "))
mes = int(input("Digite o mês do nascimento: "))

# Determina o signo
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
	print("Seu signo é Áries")
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
	print("Seu signo é Touro")
elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
	print("Seu signo é Gêmeos")
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
	print("Seu signo é Câncer")
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
	print("Seu signo é Leão")
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
	print("Seu signo é Virgem")
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
	print("Seu signo é Libra")
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
	print("Seu signo é Escorpião")
elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
	print("Seu signo é Sagitário")
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
	print("Seu signo é Capricórnio")
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
	print("Seu signo é Aquário")
elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
	print("Seu signo é Peixes")
else:
	print("Data inválida!")
