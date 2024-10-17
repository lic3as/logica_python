# módulo com as funções encontrar_maximo, encontrar_minimo, calcular_media e ordenar_lista envolvendo listas

def encontrar_maximo(lista):
    return max(lista)  # função interna para encontrar o máximo entre uma lista

def encontrar_minimo(lista):
    return min(lista)  # função interna para encontrar o mínimo entre uma lista

def calcular_media(lista):
    return sum(lista) / len(lista) # função interna para encontrar a soma dos elementos da lista (sum) e para o tamanho da lista (len)
    # soma / tamanho resulta na média

def ordenar_lista(lista):
    return sorted(lista)   # função interna para ordenar os elementos de uma lista
