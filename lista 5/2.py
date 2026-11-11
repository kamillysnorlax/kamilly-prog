def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"


numero = int(input("Digite um número: "))

resultado = verificar_par_impar(numero)

print("O número é", resultado)