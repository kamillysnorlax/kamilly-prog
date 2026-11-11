quantidade = 0
soma = 0

numero = int(input("Digite um número (0 para encerrar): "))

while numero != 0:
    quantidade += 1
    soma += numero

    numero = int(input("Digite um número (0 para encerrar): "))

if quantidade > 0:
    media = soma / quantidade
else:
    media = 0

print("\nResultado:")
print("Quantidade de números digitados:", quantidade)
print("Soma dos números:", soma)
print("Média aritmética:", media)