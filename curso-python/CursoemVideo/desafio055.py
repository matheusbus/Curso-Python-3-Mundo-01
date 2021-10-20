# Crie um programa que leia o peso de CINCO PESSOAS. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
pessoa = 1
for p in range(0, 5):
    peso = float(input('Digite o peso da {}° pessoa: '.format(pessoa)))
    if p == 0:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
    pessoa = pessoa + 1
print(' ')
print('O maior peso digitado foi de \033[41m{:.0f}\033[m Kgs.'.format(maior))
print(' ')
print('O menor peso digitado foi de \033[41m{:.0f}\033[m Kgs.'.format(menor))
