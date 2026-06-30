from _motor.colisao import (
    AREA_MAX_X,
    AREA_MAX_Y,
    AREA_MIN_X,
    AREA_MIN_Y,
    BLOQUEADAS,
    CELULA,
    COLUNAS,
    LINHAS,
)


def celula_livre(x, y):
    if x < 0 or y < 0 or x >= COLUNAS or y >= LINHAS:
        return False
    if x < AREA_MIN_X or x > AREA_MAX_X or y < AREA_MIN_Y or y > AREA_MAX_Y:
        return False
    return (x, y) not in BLOQUEADAS


def celula_para_pixel(x, y, largura_sprite, altura_sprite):
    centro_x = x * CELULA + CELULA // 2
    centro_y = y * CELULA + CELULA // 2
    px = centro_x - largura_sprite // 2
    py = centro_y - altura_sprite // 2
    return px, py


def adjacente(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2) == 1
