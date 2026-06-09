# Solicita o valor do depósito mensal
deposito = float(input("Digite o valor do depósito mensal: R$ "))

saldo = 0
juros = 0.005  # 0,5% ao mês

print("\nEvolução da poupança:")

for mes in range(1, 25):
    saldo += deposito          # faz o depósito do mês
    saldo += saldo * juros     # aplica os juros de 0,5%
    
    print(f"Mês {mes}: R$ {saldo:.2f}")

print(f"\nSaldo final após 24 meses: R$ {saldo:.2f}")