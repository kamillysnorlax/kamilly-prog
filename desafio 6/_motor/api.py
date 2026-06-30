from _motor.entidades import DIRECOES
from _motor.mundo import adjacente, celula_livre


class OrcControle:
    def __init__(self, orc, player):
        self._orc = orc
        self._player = player
        self._movimento_usado = False
        self._mover_pendente = False
        self._ataque_resultado = None
        self._ticks_ataque = 0
        self._cooldown_ticks = 5

    def reset_tick(self):
        self._movimento_usado = False
        self._mover_pendente = False
        self._ataque_resultado = None

    @property
    def ataque_resultado(self):
        return self._ataque_resultado

    @property
    def EIXO_X(self) -> int:
        return self._orc.x

    @property
    def EIXO_Y(self) -> int:
        return self._orc.y

    @property
    def ESTA_TOCANDO(self) -> bool:
        return adjacente(self._orc.x, self._orc.y, self._player.x, self._player.y)

    @property
    def PLAYER_A_FRENTE(self) -> bool:
        fx, fy = self._orc.frente()
        return self._player.x == fx and self._player.y == fy

    @property
    def PAREDE_A_FRENTE(self) -> bool:
        fx, fy = self._orc.frente()
        return not celula_livre(fx, fy)

    def mover_frente(self) -> None:
        if self._movimento_usado:
            return
        self._movimento_usado = True
        self._mover_pendente = True

    def virar_esquerda(self) -> None:
        self._orc.virar_esquerda()

    def virar_direita(self) -> None:
        self._orc.virar_direita()

    def atacar(self) -> None:
        if self._ticks_ataque < self._cooldown_ticks:
            self._ataque_resultado = "falha_cooldown"
            return
        if self.ESTA_TOCANDO:
            self._ataque_resultado = "acerto"
        else:
            self._ataque_resultado = "falha_distancia"

    def aplicar_movimento(self) -> None:
        if not self._mover_pendente:
            return
        dx, dy = DIRECOES[self._orc.facing]
        self._orc.mover(dx, dy, celula_livre)

    def avancar_cooldown(self) -> None:
        self._ticks_ataque += 1

    def registrar_acerto(self) -> None:
        self._ticks_ataque = 0

    def executar(self, inteligencia_orc) -> None:
        inteligencia_orc(self)
