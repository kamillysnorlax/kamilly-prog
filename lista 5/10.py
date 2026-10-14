import random

def embaralhar(texto):
    texto = texto.lower()
    lista = list(texto)
    random.shuffle(lista)
    return "".join(lista)


palavra = input("Digite uma palavra: ")

resultado = embaralhar(palavra)

print("Palavra embaralhada:", resultado)