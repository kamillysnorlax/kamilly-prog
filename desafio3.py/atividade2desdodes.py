from deep_translator import GoogleTranslator

texto_original = "Eu gosto de aprender programação e criar projetos em Python."

print("TEXTO ORIGINAL:")
print(texto_original)

idiomas = [
    "ingles", "espanhol", "frances", "alemao", "italiano",
    "japones", "chines", "russo", "arabe", "portugues"
]

texto = texto_original

# pequenas "transformações" que simulam perda de sentido
mudancas = [
    ("gosto de", "curto"),
    ("aprender", "estudar"),
    ("programação", "codificação"),
    ("criar projetos", "fazer coisas"),
    ("Python", "uma linguagem")
]

for idioma in idiomas:
    for antigo, novo in mudancas:
        texto = texto.replace(antigo, novo)

    texto = f"{texto} -> traduzido em {idioma}"

print("\nTEXTO FINAL:")
print(texto)
