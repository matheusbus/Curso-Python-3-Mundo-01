# Crie um programa que leia o primeiro termo de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

import time

print('\033[1;45m~~\033[m' * 20)
print('\033[1;45mP R O G R E S S Ã O  A R I T M É T I C A\033[m')
print('\033[1;45m~~\033[m' * 20)

i = int(input('Digite o primeiro termo da PA: '))
p = int(input('Digite a razão da PA: '))
dectermo = i + (10-1) * p
print('Working...')
time.sleep(1)
for c in range(i, dectermo + p, p):
    print('->', c, end= ' ')
    time.sleep(0.5)
print('ACABOU')
