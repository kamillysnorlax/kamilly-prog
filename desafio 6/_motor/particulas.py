import math
import random

import pygame


class Particula:
    __slots__ = ("x", "y", "vx", "num", "vy", "vida", "vida_max", "cor", "tamanho", "gravidade")

    def __init__(self, x, y, vx, vy, vida, cor, tamanho, gravidade=0.0):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.vida = vida
        self.vida_max = vida
        self.cor = cor
        self.tamanho = tamanho
        self.gravidade = gravidade

    def atualizar(self, delta):
        self.vida -= delta
        self.vx *= 0.98
        self.vy += self.gravidade * delta * 0.06
        self.vy *= 0.98
        self.x += self.vx * delta * 0.06
        self.y += self.vy * delta * 0.06
        return self.vida > 0


class GerenciadorParticulas:
    def __init__(self):
        self._particulas = []

    def _emitir(self, x, y, quantidade, cores, velocidade, vida, tamanho, gravidade=0.0, spread=6.28):
        for _ in range(quantidade):
            angulo = random.uniform(0, spread) if spread >= 6.0 else random.uniform(-spread, spread)
            vel = random.uniform(velocidade * 0.4, velocidade)
            vx = math.cos(angulo) * vel
            vy = math.sin(angulo) * vel
            cor = random.choice(cores)
            vida_p = random.uniform(vida * 0.6, vida)
            tam = random.uniform(tamanho * 0.6, tamanho)
            self._particulas.append(Particula(x, y, vx, vy, vida_p, cor, tam, gravidade))

    def poeira_passo(self, x, y, dx, dy):
        px = x - dx * 3
        py = y + 4
        cores = [(180, 150, 110, 180), (140, 120, 90, 160), (200, 180, 140, 140)]
        angulo = math.atan2(dy, dx) + math.pi
        for _ in range(4):
            vel = random.uniform(0.8, 2.2)
            vx = math.cos(angulo + random.uniform(-0.6, 0.6)) * vel
            vy = math.sin(angulo + random.uniform(-0.6, 0.6)) * vel
            cor = random.choice(cores)
            self._particulas.append(Particula(px, py, vx, vy, random.uniform(180, 320), cor, random.uniform(2, 4), 0.15))

    def ataque_falha(self, x, y):
        self._emitir(x, y, 10, [(255, 230, 80, 220), (255, 200, 50, 200), (255, 255, 160, 180)], 3.5, 350, 4)

    def ataque_acerto(self, x, y):
        self._emitir(x, y, 18, [(255, 60, 50, 240), (255, 120, 60, 220), (255, 200, 80, 200)], 5.0, 500, 5, 0.08)
        self._emitir(x, y, 8, [(255, 255, 220, 200), (255, 180, 100, 180)], 2.5, 400, 3)

    def vitoria_confete(self, largura, altura):
        x = random.uniform(0, largura)
        y = random.uniform(-20, -5)
        cores = [
            (255, 210, 70, 230), (255, 90, 90, 230), (90, 200, 255, 230),
            (130, 255, 130, 230), (255, 150, 220, 230),
        ]
        cor = random.choice(cores)
        vx = random.uniform(-1.5, 1.5)
        vy = random.uniform(2.0, 5.0)
        self._particulas.append(Particula(x, y, vx, vy, random.uniform(2000, 3500), cor, random.uniform(3, 6), 0.12))

    def atualizar(self, delta, vitoria=False, largura=800, altura=800):
        if vitoria and random.random() < 0.35:
            self.vitoria_confete(largura, altura)
        self._particulas = [p for p in self._particulas if p.atualizar(delta)]

    def desenhar(self, tela):
        for p in self._particulas:
            alpha = max(0, min(255, int(255 * (p.vida / p.vida_max))))
            cor = (*p.cor[:3], alpha) if len(p.cor) == 4 else (*p.cor, alpha)
            surf = pygame.Surface((int(p.tamanho * 2), int(p.tamanho * 2)), pygame.SRCALPHA)
            pygame.draw.circle(surf, cor, (int(p.tamanho), int(p.tamanho)), max(1, int(p.tamanho)))
            tela.blit(surf, (int(p.x - p.tamanho), int(p.y - p.tamanho)))
