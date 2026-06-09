# Solicita um número ao usuário
numero = int(input("Digite um número: "))

print(f"Tabuada do número {numero}")

# Exibe a tabuada de 1 a 10
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")