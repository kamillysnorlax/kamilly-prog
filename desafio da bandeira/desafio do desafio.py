
import os
import time

VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
BRANCO = "\033[37m"
RESET = "\033[0m"


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


bandeira = f"""
{VERDE}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋{AZUL}⣀⣠⣤⣤⣄⣀{VERDE}⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣿⣿⣿⠿⠛⠉{AMARELO}⠄{AZUL}⢠⣾⣿⣿⣿⣿⣿⣿⣷⡄{AMARELO}⠄{VERDE}⠉⠛⠿⣿⣿⣿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⠿⠛⠁{AMARELO}⠄⠄⠄⠄{AZUL}⣔⣷⣷⣦⣤⣬⣹⡛⠿⣿⡄{AMARELO}⠄⠄⠄⠄{VERDE}⠙⠿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣶⣄⡀{AMARELO}⠄⠄⠄⠄{AZUL}⣿⣻⢿⣿⣿⣟⣿⣿⡾⣌⠁{AMARELO}⠄⠄⠄⠄{VERDE}⣠⣴⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣿⣿⣿⣶⣤⡀{AMARELO}⠄{AZUL}⠘⢿⣿⣿⣿⣿⣽⣏⡿⠃{AMARELO}⠄{VERDE}⢀⣤⣶⣿⣿⣿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄{AZUL}⠉{AZUL}⠙⠛⠛⠛⠉{VERDE}⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{RESET}
{VERDE}⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿{RESET}
"""

texto = """
88                                                        88 88
88                                                        "  88 
88                                                           88
88,dPPYba,      8b,dPPYba,     ,adPPYYba,   888888888    88  88
88'      "8a    88P'    "Y8   " "      `Y        a8P"    88  88
88        d8    88             ,adPPPPP88     ,d8P'      88  88
88b,     ,a8"   88             88,    ,88   ,d8"         88  88
8Y"Ybbd8"'      88             `"8bbdP"Y8   888888888    88  88
"""

while True:
    limpar_tela()
    print(bandeira)
    time.sleep(3)

    limpar_tela()
    print(texto)
    time.sleep(3)
