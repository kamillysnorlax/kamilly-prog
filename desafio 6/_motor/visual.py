import math

import pygame

from _motor.colisao import CELULA
from _motor.entidades import ANGULOS_FACING


class AnimadorAtor:
    def __init__(self, ator):
        self._ator = ator
        self.inicio_x = float(ator.x)
        self.inicio_y = float(ator.y)
        self.rotacao = 0.0
        self._rotacao_alvo = 0.0
        self._inclinacao_andar = 0.0
        self._pulo = None

    @property
    def em_pulo(self):
        return self._pulo is not None

    def iniciar_pulo(self, ix, iy, fx, fy, duracao=480):
        self._pulo = {"ix": float(ix), "iy": float(iy), "fx": float(fx), "fy": float(fy), "t": 0.0, "dur": duracao}

    def iniciar_tick(self):
        if self.em_pulo:
            return
        self.inicio_x = float(self._ator.x)
        self.inicio_y = float(self._ator.y)

    def notificar_movimento(self):
        if self.em_pulo:
            return
        mov = self._ator.ultimo_movimento
        if mov:
            dx, dy = mov
            self._inclinacao_andar = math.sin(pygame.time.get_ticks() * 0.02) * 4
            if dx != 0:
                self._rotacao_alvo = 10 if dx > 0 else -10
            else:
                self._rotacao_alvo = 6 if dy > 0 else -6
        else:
            self._rotacao_alvo = ANGULOS_FACING[self._ator.facing] * 0.35

    def posicao_interpolada(self, progresso):
        if self._pulo:
            p = self._pulo
            t = min(1.0, p["t"] / p["dur"])
            ease = t * t * (3 - 2 * t)
            gx = p["ix"] + (p["fx"] - p["ix"]) * ease
            gy = p["iy"] + (p["fy"] - p["iy"]) * ease
            gy -= math.sin(t * math.pi) * 0.85
            return gx, gy
        t = progresso * progresso * (3 - 2 * progresso)
        gx = self.inicio_x + (self._ator.x - self.inicio_x) * t
        gy = self.inicio_y + (self._ator.y - self.inicio_y) * t
        return gx, gy

    def escala_desenho(self):
        if not self._pulo:
            return 1.0, 1.0
        t = min(1.0, self._pulo["t"] / self._pulo["dur"])
        if t < 0.14:
            k = t / 0.14
            return 1.0 + 0.28 * k, 1.0 - 0.48 * k
        if t > 0.86:
            k = (t - 0.86) / 0.14
            return 1.28 - 0.28 * k, 0.52 + 0.48 * k
        return 1.06, 1.1

    def atualizar(self, delta, progresso):
        if self._pulo:
            self._pulo["t"] += delta
            if self._pulo["t"] >= self._pulo["dur"]:
                self._pulo = None
        mov = self._ator.ultimo_movimento
        if self.em_pulo:
            self._rotacao_alvo = 0
        elif mov and progresso < 1.0:
            self._rotacao_alvo = (10 if mov[0] > 0 else -10 if mov[0] < 0 else 6 if mov[1] > 0 else -6)
            self._inclinacao_andar = math.sin(progresso * math.pi * 2) * 3
        else:
            self._inclinacao_andar *= 0.85
            self._rotacao_alvo = ANGULOS_FACING[self._ator.facing] * 0.25
        self.rotacao += (self._rotacao_alvo + self._inclinacao_andar - self.rotacao) * min(1.0, delta * 0.012)


def centro_celula(gx, gy):
    return gx * CELULA + CELULA // 2, gy * CELULA + CELULA // 2


def desenhar_personagem(tela, sprite, gx, gy, rotacao=0.0, espelhar=False, tinte=None, escala_x=1.0, escala_y=1.0):
    imagem = pygame.transform.flip(sprite, espelhar, False) if espelhar else sprite
    if escala_x != 1.0 or escala_y != 1.0:
        largura = max(1, int(imagem.get_width() * escala_x))
        altura = max(1, int(imagem.get_height() * escala_y))
        imagem = pygame.transform.smoothscale(imagem, (largura, altura))
    if abs(rotacao) > 0.01:
        imagem = pygame.transform.rotate(imagem, -rotacao)
    if tinte:
        copia = imagem.copy()
        copia.fill(tinte, special_flags=pygame.BLEND_RGBA_MULT)
        imagem = copia
    cx, cy = centro_celula(gx, gy)
    rect = imagem.get_rect(center=(int(cx), int(cy)))
    tela.blit(imagem, rect)
    return cx, cy


class AnimacaoAtaqueOrc:
    def __init__(self):
        self._ativo = False
        self._gx_orc = 0.0
        self._gy_orc = 0.0
        self._gx_alvo = 0.0
        self._gy_alvo = 0.0
        self._tempo_restante = 0
        self._duracao = 420

    def disparar(self, gx_orc, gy_orc):
        self._ativo = True
        self._gx_orc = gx_orc
        self._gy_orc = gy_orc
        self._gx_alvo = gx_orc
        self._gy_alvo = gy_orc
        self._tempo_restante = self._duracao

    def marcar_alvo(self, gx, gy):
        self._gx_alvo = gx
        self._gy_alvo = gy

    def atualizar(self, delta):
        if not self._ativo:
            return
        self._tempo_restante -= delta
        if self._tempo_restante <= 0:
            self._ativo = False

    @property
    def ativo(self):
        return self._ativo

    def _desenhar_bola(self, tela, gx, gy, progresso, raio_base=10):
        cx, cy = centro_celula(gx, gy)
        cy_pes = cy + CELULA // 2 + 2
        pulso = math.sin(progresso * math.pi)
        raio = int(raio_base + pulso * 12)
        alpha = int(160 + pulso * 80)
        surf = pygame.Surface((raio * 2 + 6, raio * 2 + 6), pygame.SRCALPHA)
        centro = raio + 3
        pygame.draw.circle(surf, (255, 50, 40, alpha // 2), (centro, centro), raio + 3)
        pygame.draw.circle(surf, (255, 70, 55, alpha), (centro, centro), raio)
        pygame.draw.circle(surf, (255, 160, 140, min(255, alpha + 40)), (centro, centro), max(3, raio // 2))
        tela.blit(surf, (int(cx - centro), int(cy_pes - centro)))

    def desenhar(self, tela):
        if not self._ativo:
            return
        progresso = 1.0 - (self._tempo_restante / self._duracao)
        self._desenhar_bola(tela, self._gx_orc, self._gy_orc, progresso, raio_base=12)
        if (self._gx_alvo, self._gy_alvo) != (self._gx_orc, self._gy_orc):
            self._desenhar_bola(tela, self._gx_alvo, self._gy_alvo, progresso, raio_base=8)


def formatar_tempo(ms):
    total = ms / 1000.0
    minutos = int(total // 60)
    segundos = total % 60
    return f"{minutos:02d}:{segundos:05.2f}"


def desenhar_temporizador(tela, tempo_ms):
    fonte = pygame.font.SysFont("arial", 22, bold=True)
    texto = formatar_tempo(tempo_ms)
    rotulo = fonte.render(texto, True, (255, 245, 210))
    fundo = pygame.Surface((rotulo.get_width() + 20, rotulo.get_height() + 10), pygame.SRCALPHA)
    fundo.fill((0, 0, 0, 120))
    x = tela.get_width() - fundo.get_width() - 12
    y = 10
    tela.blit(fundo, (x, y))
    tela.blit(rotulo, (x + 10, y + 5))


class TelaVitoria:
    def __init__(self, largura, altura):
        self._largura = largura
        self._altura = altura
        self._tempo = 0
        self._tempo_vitoria_ms = 0
        self._fonte_titulo = pygame.font.SysFont("arial", 52, bold=True)
        self._fonte_sub = pygame.font.SysFont("arial", 24)
        self._fonte_hint = pygame.font.SysFont("arial", 18)

    def definir_tempo(self, tempo_ms):
        self._tempo_vitoria_ms = tempo_ms

    def atualizar(self, delta):
        self._tempo += delta

    def desenhar(self, tela):
        overlay = pygame.Surface((self._largura, self._altura), pygame.SRCALPHA)
        alpha = min(200, int(120 + self._tempo * 0.08))
        overlay.fill((10, 5, 20, alpha))
        tela.blit(overlay, (0, 0))

        pulso = 1.0 + math.sin(self._tempo * 0.004) * 0.06
        titulo_base = self._fonte_titulo.render("Vitoria!", True, (255, 220, 80))
        tw = max(1, int(titulo_base.get_width() * pulso))
        th = max(1, int(titulo_base.get_height() * pulso))
        titulo = pygame.transform.smoothscale(titulo_base, (tw, th))
        brilho = self._fonte_titulo.render("Vitoria!", True, (255, 255, 200))
        brilho.set_alpha(80 + int(40 * math.sin(self._tempo * 0.006)))
        cx, cy = self._largura // 2, self._altura // 2 - 50
        tela.blit(brilho, brilho.get_rect(center=(cx, cy)))
        tela.blit(titulo, titulo.get_rect(center=(cx, cy)))

        sub = self._fonte_sub.render("O orc derrotou o aventureiro.", True, (240, 230, 210))
        tela.blit(sub, sub.get_rect(center=(cx, cy + 45)))

        tempo_txt = self._fonte_sub.render(
            f"Tempo: {formatar_tempo(self._tempo_vitoria_ms)}", True, (255, 210, 100),
        )
        tela.blit(tempo_txt, tempo_txt.get_rect(center=(cx, cy + 82)))

        if int(self._tempo / 500) % 2 == 0:
            hint = self._fonte_hint.render("Pressione qualquer tecla para sair.", True, (190, 190, 190))
            tela.blit(hint, hint.get_rect(center=(cx, cy + 120)))

        raio = 60 + int(10 * math.sin(self._tempo * 0.005))
        cor_anel = (255, 180, 60, 40)
        anel = pygame.Surface((raio * 2, raio * 2), pygame.SRCALPHA)
        pygame.draw.circle(anel, cor_anel, (raio, raio), raio, 3)
        tela.blit(anel, anel.get_rect(center=(cx, cy)))
