import math

def calcular_volume(altura, raio):
    volume = math.pi * raio ** 2 * altura
    return volume


altura = float(input("Digite a altura do cilindro em metros: "))
raio = float(input("Digite o raio do cilindro em metros: "))

volume = calcular_volume(altura, raio)

print("Volume do cilindro:", volume, "m³")