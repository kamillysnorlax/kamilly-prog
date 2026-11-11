import sys
from pathlib import Path

import pygame

from _motor.api import OrcControle
from _motor.colisao import CELULA, COLUNAS, LINHAS, POSICAO_ORC, POSICAO_PLAYER
from _motor.entidades import Ator
from _motor.particulas import GerenciadorParticulas
from _motor.player_ia import PlayerIA
from _motor.visual import (
    AnimacaoAtaqueOrc,
    AnimadorAtor,
    TelaVitoria,
    centro_celula,
    desenhar_personagem,
    desenhar_temporizador,
)

TICK_MS = 100
FPS = 60
ATAQUE_COOLDOWN_TICKS = 5
ESCALA_SPRITE = 3
PASTA_ASSETS = Path(__file__).resolve().parent.parent / "assets"


def _carregar_cena(caminho):
    return pygame.image.load(str(caminho)).convert()


def _carregar_personagem(caminho, escala=ESCALA_SPRITE):
    imagem = pygame.image.load(str(caminho)).convert_alpha()
    if escala != 1:
        largura = imagem.get_width() * escala
        altura = imagem.get_height() * escala
        imagem = pygame.transform.scale(imagem, (largura, altura))
    return imagem


def _emitir_poeira(particulas, animador, ator):
    if not ator.ultimo_movimento:
        return
    gx, gy = animador.posicao_interpolada(1.0)
    cx, cy = centro_celula(gx, gy)
    dx, dy = ator.ultimo_movimento
    particulas.poeira_passo(cx, cy, dx, dy)


def _disparar_ataque_visual(anim_ataque, orc, player, resultado):
    anim_ataque.disparar(float(orc.x), float(orc.y))
    if resultado == "acerto":
        anim_ataque.marcar_alvo(float(player.x), float(player.y))
    else:
        fx, fy = orc.frente()
        anim_ataque.marcar_alvo(float(fx), float(fy))


def executar_simulacao(inteligencia_orc):
    pygame.init()
    pygame.display.set_caption("Desafio 6 - IA do Orc")

    largura = COLUNAS * CELULA
    altura = LINHAS * CELULA
    tela = pygame.display.set_mode((largura, altura))

    cena = _carregar_cena(PASTA_ASSETS / "scene.png")
    sprite_player = _carregar_personagem(PASTA_ASSETS / "player.png")
    sprite_orc = _carregar_personagem(PASTA_ASSETS / "orc.png")
    relogio = pygame.time.Clock()

    player = Ator(*POSICAO_PLAYER, facing=0)
    orc = Ator(*POSICAO_ORC, facing=2)
    anim_player = AnimadorAtor(player)
    anim_orc = AnimadorAtor(orc)
    ia_player = PlayerIA()
    api = OrcControle(orc, player)
    api._ticks_ataque = ATAQUE_COOLDOWN_TICKS
    particulas = GerenciadorParticulas()
    tela_vitoria = TelaVitoria(largura, altura)
    anim_ataque_orc = AnimacaoAtaqueOrc()

    tempo_acumulado = 0
    cronometro_ms = 0
    vitoria = False
    orc_tinte = None
    player_tinte = None
    flash_orc_ms = 0
    flash_player_ms = 0

    rodando = True
    while rodando:
        delta = relogio.tick(FPS)
        progresso_tick = min(1.0, tempo_acumulado / TICK_MS) if TICK_MS else 1.0

        if not vitoria:
            cronometro_ms += delta
            tempo_acumulado += delta
            while tempo_acumulado >= TICK_MS:
                tempo_acumulado -= TICK_MS
                progresso_tick = tempo_acumulado / TICK_MS

                player.reset_movimento()
                orc.reset_movimento()
                ia_player.reset_ataque()
                ia_player.reset_pulo()
                anim_player.iniciar_tick()
                anim_orc.iniciar_tick()

                api.reset_tick()
                pulo_info = ia_player.passo(player, orc, TICK_MS)
                if pulo_info:
                    ox, oy, nx, ny = pulo_info
                    anim_player.iniciar_pulo(ox, oy, nx, ny)
                    cx1, cy1 = centro_celula(float(ox), float(oy))
                    cx2, cy2 = centro_celula(float(nx), float(ny))
                    dx = 1 if nx > ox else -1 if nx < ox else 0
                    dy = 1 if ny > oy else -1 if ny < oy else 0
                    particulas.poeira_passo(cx1, cy1, dx, dy)
                    particulas.poeira_passo(cx2, cy2, dx, dy)
                ia_player.tentar_ataque(player, orc)
                api.executar(inteligencia_orc)
                api.aplicar_movimento()
                api.avancar_cooldown()
                ia_player.avancar_cooldown()

                anim_player.notificar_movimento()
                anim_orc.notificar_movimento()
                _emitir_poeira(particulas, anim_player, player)
                _emitir_poeira(particulas, anim_orc, orc)

                ataque_player = ia_player.ultimo_ataque
                if ataque_player in ("falha_cooldown", "acerto"):
                    px, py = centro_celula(float(player.x), float(player.y))
                    if ataque_player == "acerto":
                        player_tinte = (120, 180, 255, 255)
                        flash_player_ms = 180
                        orc_tinte = (255, 120, 80, 255)
                        flash_orc_ms = 220
                        particulas.ataque_acerto(px, py)
                    else:
                        player_tinte = (255, 255, 80, 255)
                        flash_player_ms = 120
                        particulas.ataque_falha(px, py)

                resultado = api.ataque_resultado
                if resultado in ("falha_cooldown", "falha_distancia", "acerto"):
                    _disparar_ataque_visual(anim_ataque_orc, orc, player, resultado)
                    ox, oy = centro_celula(float(orc.x), float(orc.y))
                    if resultado == "falha_cooldown" or resultado == "falha_distancia":
                        orc_tinte = (255, 255, 80, 255)
                        flash_orc_ms = 180
                        particulas.ataque_falha(ox, oy)
                    elif resultado == "acerto":
                        orc_tinte = (255, 80, 80, 255)
                        player_tinte = (255, 80, 80, 255)
                        flash_orc_ms = 400
                        flash_player_ms = 400
                        particulas.ataque_acerto(ox, oy)
                        px, py = centro_celula(float(player.x), float(player.y))
                        particulas.ataque_acerto(px, py)
                        api.registrar_acerto()
                        vitoria = True
                        tela_vitoria.definir_tempo(cronometro_ms)
                        for _ in range(40):
                            particulas.vitoria_confete(largura, altura)
                        break

        progresso_tick = min(1.0, tempo_acumulado / TICK_MS) if not vitoria else 1.0
        anim_player.atualizar(delta, progresso_tick)
        anim_orc.atualizar(delta, progresso_tick)
        anim_ataque_orc.atualizar(delta)

        if flash_orc_ms > 0 and not vitoria:
            flash_orc_ms -= delta
            if flash_orc_ms <= 0:
                orc_tinte = None
        if flash_player_ms > 0 and not vitoria:
            flash_player_ms -= delta
            if flash_player_ms <= 0:
                player_tinte = None

        particulas.atualizar(delta, vitoria=vitoria, largura=largura, altura=altura)
        if vitoria:
            tela_vitoria.atualizar(delta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            elif vitoria and evento.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                rodando = False

        tela.blit(cena, (0, 0))

        gx_p, gy_p = anim_player.posicao_interpolada(progresso_tick)
        gx_o, gy_o = anim_orc.posicao_interpolada(progresso_tick)

        escala_px, escala_py = anim_player.escala_desenho()
        desenhar_personagem(
            tela, sprite_player, gx_p, gy_p, anim_player.rotacao,
            tinte=player_tinte, escala_x=escala_px, escala_y=escala_py,
        )

        if anim_ataque_orc.ativo:
            anim_ataque_orc.desenhar(tela)

        desenhar_personagem(
            tela, sprite_orc, gx_o, gy_o, anim_orc.rotacao,
            espelhar=orc.facing in (0, 2), tinte=orc_tinte,
        )

        particulas.desenhar(tela)

        if not vitoria:
            desenhar_temporizador(tela, cronometro_ms)

        if vitoria:
            tela_vitoria.desenhar(tela)

        pygame.display.flip()

    pygame.quit()
    sys.exit(0)
