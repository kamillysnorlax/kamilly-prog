# Valor inicial da dívida
divida = 1000.00

# Quantidade de meses
meses = int(input("Digite a quantidade de meses: "))

# Taxa de juros mensal (10%)
juros = 10

# Calcula a dívida mês a mês
for i in range(meses):
    divida = divida + (divida * juros / 100)

# Exibe o valor final da dívida
print(f"Dívida após {meses} meses: R$ {divida:.2f}")