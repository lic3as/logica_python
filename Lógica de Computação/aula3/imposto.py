# informar a renda
# calcular o imposto a partir da renda (<=2000: não paga imposto, <=5000: 10% da renda, >5000: 20% da renda)
# imprimir o valor do imposto a pagar

print('CÁLCULO DE IMPOSTO')
renda = float(input('Informe a renda anual: '))

if renda <= 2000:
    imposto = 0
elif renda <= 5000:
    imposto = renda * 0.1
else:
    imposto = renda * 0.2

print(f'O imposto a pagar é: R$ {imposto:.2f}.')
