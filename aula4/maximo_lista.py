# fazer uma função que receba uma lista e informe o valor máximo contido nela

def encontrar_maximo(lista):
    max = lista[0]
    for num in lista:
        if num > max:
            max = num
    return max

lista = list()
for c in range(5):
    lista.append(int(input(f'Informe o valor {c} da lista: ')))
print(f'Lista: {lista}')
print(f'O valor máximo contido na lista é {encontrar_maximo(lista)}')
