# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares,
# Se o valor digitado for ímpar, desconsidere-o.

s = 0
i = 0
for c in range(0,6):
    n = int(input('Digite um número par: '))
    if n % 2 == 0:
        s = s + n
    else:
        i = i + 1
if i != 0:
    print('{} números digitados foram ímpares.'.format(i))
    print('Os valores ímpares foram desconsiderados da soma.')
print('A soma dos valores pares é igual a {}.'.format(s))
