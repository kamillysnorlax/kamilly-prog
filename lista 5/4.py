def calcular_soma(lista):
    return sum(lista)


numeros = []

for i in range(4):
    numero = float(input("Digite um número: "))
    numeros.append(numero)

soma = calcular_soma(numeros)

print("Soma:", soma)