def lista_vazia(lista):
    return len(lista) == 0


def maior_valor(lista):
    if lista_vazia(lista):
        return -1
    return max(lista)


def menor_valor(lista):
    if lista_vazia(lista):
        return -1
    return min(lista)


def valor_medio(lista):
    if lista_vazia(lista):
        return -1
    return sum(lista) / len(lista)


lista_vazia_teste = []
lista_com_elementos = [10, 20, 30, 40, 50]

print("LISTA VAZIA")
print("Está vazia?", lista_vazia(lista_vazia_teste))
print("Maior valor:", maior_valor(lista_vazia_teste))
print("Menor valor:", menor_valor(lista_vazia_teste))
print("Valor médio:", valor_medio(lista_vazia_teste))

print("\nLISTA COM ELEMENTOS")
print("Está vazia?", lista_vazia(lista_com_elementos))
print("Maior valor:", maior_valor(lista_com_elementos))
print("Menor valor:", menor_valor(lista_com_elementos))
print("Valor médio:", valor_medio(lista_com_elementos))