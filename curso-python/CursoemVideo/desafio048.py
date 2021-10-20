# Crie um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
# que se encontram no intervalo entre 1 até 500.

s = 0
t = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        print(c, end= ' ')
        t = t + 1
print()
print('A soma de todos os {} valores é igual a {}.'.format(t, s))
