import random

from _motor.mundo import adjacente, celula_livre

DIRECOES = ((0, -1), (0, 1), (-1, 0), (1, 0))
MAX_PASSOS_MESMA_DIRECAO = 5
CHANCE_MANTER_DIRECAO = 0.78
FUGA_MS = 3000
PULO_MS = 3000
CHANCE_PULO = 0.22
DISTANCIA_PULO = 5
ATAQUE_COOLDOWN_TICKS = 5


class PlayerIA:
    def __init__(self):
        self._direcao = random.choice(DIRECOES)
        self._passos_na_direcao = 0
        self._tempo_fuga = 0
        self._tempo_pulo = 0
        self._ticks_ataque = ATAQUE_COOLDOWN_TICKS
        self._ultimo_ataque = None
        self._ultimo_pulo = None

    @property
    def ultimo_ataque(self):
        return self._ultimo_ataque

    @property
    def ultimo_pulo(self):
        return self._ultimo_pulo

    def reset_ataque(self):
        self._ultimo_ataque = None

    def reset_pulo(self):
        self._ultimo_pulo = None

    def _trocar_direcao(self):
        opcoes = [d for d in DIRECOES if d != self._direcao]
        self._direcao = random.choice(opcoes)
        self._passos_na_direcao = 0

    def _decidir_direcao(self):
        if self._passos_na_direcao >= MAX_PASSOS_MESMA_DIRECAO:
            self._trocar_direcao()
            return
        if self._passos_na_direcao == 0:
            return
        if random.random() >= CHANCE_MANTER_DIRECAO:
            self._trocar_direcao()

    def _direcoes_fuga(self, player, orc):
        dx = player.x - orc.x
        dy = player.y - orc.y
        candidatos = []
        if dx > 0:
            candidatos.append((1, 0))
        elif dx < 0:
            candidatos.append((-1, 0))
        if dy > 0:
            candidatos.append((0, 1))
        elif dy < 0:
            candidatos.append((0, -1))
        if not candidatos:
            return []
        random.shuffle(candidatos)
        return candidatos

    def _tentar_fuga(self, player, orc):
        for dx, dy in self._direcoes_fuga(player, orc):
            if player.mover(dx, dy, celula_livre):
                self._direcao = (dx, dy)
                self._passos_na_direcao = 1
                return True
        return False

    def _tentar_pulo(self, player):
        if random.random() > CHANCE_PULO:
            return None
        dx, dy = self._direcao
        resultado = player.pular_para(dx, dy, DISTANCIA_PULO, celula_livre)
        if not resultado:
            return None
        ox, oy, nx, ny, passos = resultado
        self._passos_na_direcao = passos
        self._ultimo_pulo = (ox, oy, nx, ny)
        return self._ultimo_pulo

    def _passo_aleatorio(self, player):
        self._decidir_direcao()
        dx, dy = self._direcao
        if player.mover(dx, dy, celula_livre):
            self._passos_na_direcao += 1
            return
        self._trocar_direcao()
        dx, dy = self._direcao
        if player.mover(dx, dy, celula_livre):
            self._passos_na_direcao = 1

    def passo(self, player, orc, tick_ms=100):
        self._tempo_pulo += tick_ms
        self._tempo_fuga += tick_ms

        if self._tempo_pulo >= PULO_MS:
            self._tempo_pulo = 0
            pulo = self._tentar_pulo(player)
            if pulo:
                return pulo

        if self._tempo_fuga >= FUGA_MS:
            self._tempo_fuga = 0
            if self._tentar_fuga(player, orc):
                return None

        self._passo_aleatorio(player)
        return None

    def tentar_ataque(self, player, orc):
        if not adjacente(player.x, player.y, orc.x, orc.y):
            return None
        if self._ticks_ataque < ATAQUE_COOLDOWN_TICKS:
            self._ultimo_ataque = "falha_cooldown"
            return self._ultimo_ataque
        self._ticks_ataque = 0
        self._ultimo_ataque = "acerto"
        return self._ultimo_ataque

    def avancar_cooldown(self):
        self._ticks_ataque += 1
