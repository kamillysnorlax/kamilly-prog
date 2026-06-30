import random

DIRECOES = ((1, 0), (0, 1), (-1, 0), (0, -1))
ANGULOS_FACING = (8, 5, -8, -5)


class Ator:
    def __init__(self, x, y, facing=0):
        self.x = x
        self.y = y
        self.facing = facing % 4
        self.ultimo_movimento = None

    def frente(self):
        dx, dy = DIRECOES[self.facing]
        return self.x + dx, self.y + dy

    def virar_esquerda(self):
        self.facing = (self.facing - 1) % 4

    def virar_direita(self):
        self.facing = (self.facing + 1) % 4

    def reset_movimento(self):
        self.ultimo_movimento = None

    def mover(self, dx, dy, mundo_livre):
        nx, ny = self.x + dx, self.y + dy
        if mundo_livre(nx, ny):
            self.x, self.y = nx, ny
            self.ultimo_movimento = (dx, dy)
            return True
        self.ultimo_movimento = None
        return False

    def pular_para(self, dx, dy, distancia, mundo_livre):
        passos = 0
        for i in range(1, distancia + 1):
            nx, ny = self.x + dx * i, self.y + dy * i
            if not mundo_livre(nx, ny):
                break
            passos = i
        if passos == 0:
            self.ultimo_movimento = None
            return None
        origem = (self.x, self.y)
        self.x = origem[0] + dx * passos
        self.y = origem[1] + dy * passos
        self.ultimo_movimento = (dx, dy)
        return origem[0], origem[1], self.x, self.y, passos
