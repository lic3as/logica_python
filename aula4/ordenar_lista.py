# criar uma função para fazer a ordenação de uma lista

def ordenar_lista(lista):
    return sorted(lista)

lista = list()
for c in range(5):
    lista.append(int(input(f'Informe o valor {c} da lista: ')))
print(f'Lista: {lista}')
print(f'Lista ordenada: {ordenar_lista(lista)}')
