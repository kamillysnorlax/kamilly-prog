def inteligencia_orc(orc: "Orc"):
    # MEXER APENAS AQUI
    # Sensores: orc.EIXO_X, orc.EIXO_Y, orc.ESTA_TOCANDO, orc.PLAYER_A_FRENTE, orc.PAREDE_A_FRENTE
    # Acoes: orc.mover_frente(), orc.virar_esquerda(), orc.virar_direita(), orc.atacar()

    if orc.ESTA_TOCANDO:
        if orc.PLAYER_A_FRENTE:
            orc.atacar()
        else:
            orc.virar_esquerda()
    elif not orc.PAREDE_A_FRENTE:
        orc.mover_frente()
    else:
        orc.virar_direita()

























from _motor.tipos import Orc

if __name__ == "__main__":
    from _motor import executar_simulacao

    executar_simulacao(inteligencia_orc)
