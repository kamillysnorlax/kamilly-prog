# Solicita um número ao usuário
numero = int(input("Digite um número: "))

# Se o número for positivo ou zero
if numero >= 1:
    for i in range(1, numero + 1):
        print(i)

# Se o número for negativo
elif numero <= -1:
    for i in range(1, numero - 1, -1):
        print(i)

# Se o número for zero
else:
    print(0)
