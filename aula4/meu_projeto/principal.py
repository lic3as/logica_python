# importar as funções disponíveis nos outros módulos e que serão utilizadas nessa função principal

from modulo_matematica import somar, subtrair, multiplicar, dividir
from modulo_listas import encontrar_maximo, encontrar_minimo, calcular_media, ordenar_lista

def main():
    num1 = int(input('Informe o primeiro valor: '))
    num2 = int(input('Informe o segundo valor: '))
    
    print(f'A soma entre os números é {somar(num1, num2)}.')
    print(f'A subtração entre os números é {subtrair(num1, num2)}.')
    print(f'A multiplicação entre os números é {multiplicar(num1, num2)}.')
    print(f'A divisão entre os números é {dividir(num1, num2)}.')

    lista = list()
    for c in range(5):
        num = int(input(f'Informe um valor para a posição [{c}] da lista: '))
        lista.append(num)
    print(f'O valor máximo da lista é {encontrar_maximo(lista)}.')
    print(f'O valor mínimo da lista é {encontrar_minimo(lista)}.')
    print(f'A média entre os valores da lista é {calcular_media(lista)}.')
    print(f'A lista ordenada é {ordenar_lista(lista)}.')

main()
