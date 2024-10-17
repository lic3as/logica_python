# utiilizar o laço for para imprimir os números pares de 1 a 100

print('PARES DE 1 A 100: ')
for num in range(1, 101):
    if num % 2 == 0:
        print(num, end=' | ')
print('FIM')
