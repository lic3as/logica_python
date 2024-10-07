# receber o lado do quadrado e os lados do retângulo
# criar uma função para calcular a área do quadrado e uma para a área do retângulo
# imprimir o valor das áreas

################################### FUNÇÕES ######################################
def area_quadrado(lado):
    return lado * lado

def area_retangulo(lado1, lado2):
    return lado1 * lado2

########################## ENTRADA DE DADOS ######################################
lado_q = float(input('Informe o tamanho dos lados do quadrado: '))
lado_r1 = float(input('Informe o tamanho do lado maior do retângulo: '))
lado_r2 = float(input('Informe o tamanho do lado menor do retângulo: '))

########################## SAÍDA DE DADOS #########################################
print(f'A área do quadrado é {area_quadrado(lado_q)}.')
print(f'A área do retângulo é {area_retangulo(lado_r1, lado_r2)}')
