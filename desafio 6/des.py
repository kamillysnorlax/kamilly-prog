def inteligencia_orc(orc):

    # 1. Aventureiro ao lado
    if orc.ESTA_TOCANDO:
        if orc.PLAYER_A_FRENTE:
            orc.atacar()
        else:
            orc.virar_direita()

    # 2. Persegue quando o vê
    elif orc.PLAYER_A_FRENTE:
        if not orc.PAREDE_A_FRENTE:
            orc.mover_frente()
        else:
            orc.virar_direita()

    # 3. Contorna obstáculos
    elif orc.PAREDE_A_FRENTE:
        orc.virar_direita()

    # 4. Exploração do mapa
    else:
        if (orc.EIXO_X + orc.EIXO_Y) % 2 == 0:
            orc.mover_frente()
        else:
            orc.virar_esquerda()