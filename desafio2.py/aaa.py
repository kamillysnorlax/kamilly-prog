# desafio02.py

import subprocess

nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")

subprocess.run(["git", "config", "--global", "user.name", nome])
subprocess.run(["git", "config", "--global", "user.email", email])

print("Configuração do Git aplicada com sucesso!")

# sou_kamilly.py

import subprocess

subprocess.run(["git", "config", "--global", "user.name", "Kamilly"])
subprocess.run(["git", "config", "--global", "user.email", "kamilly@escola.ifsc.edu.br"])

print("Git configurado com sucesso!")