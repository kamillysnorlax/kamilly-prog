from typing import Protocol


class Orc(Protocol):
    EIXO_X: int
    EIXO_Y: int
    ESTA_TOCANDO: bool
    PLAYER_A_FRENTE: bool
    PAREDE_A_FRENTE: bool

    def mover_frente(self) -> None: ...
    def virar_esquerda(self) -> None: ...
    def virar_direita(self) -> None: ...
    def atacar(self) -> None: ...
