# fazer uma função para calcular a média dos elementos contidos na lista

def media_lista(lista):
    tamLista = len(lista)
    somaLista = sum(lista)
    media = somaLista / tamLista
    return media

lista = list()
while True:
    num = int(input('Informe um valor para a lista: '))
    lista.append(num)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Lista: {lista}')
print(f'A média entre os valores da lista é {media_lista(lista)}')
