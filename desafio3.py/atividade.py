texto = "I like programming in Python."

# tradução manual simples (dicionário básico)
tradutor = {
    "I": "Eu",
    "like": "gosto de",
    "programming": "programar",
    "in": "em",
    "Python": "Python"
}

palavras = texto.split()
resultado = []

for p in palavras:
    resultado.append(tradutor.get(p, p))

print("Texto original:")
print(texto)

print("\nTradução para português:")
print(" ".join(resultado))
