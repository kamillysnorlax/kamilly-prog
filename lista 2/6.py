# Solicita os dados ao usuário
numero = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o início da tabuada: "))
fim = int(input("Digite o fim da tabuada: "))

print(f"\nTabuada do número {numero}")

# Exibe a tabuada do início ao fim informado
for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")