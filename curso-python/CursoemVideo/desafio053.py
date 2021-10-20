# Crie um programa que leia uma frase e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inverso = ''
for letra in range(len(juntar)-1, -1, -1):
    inverso = inverso + juntar[letra]
print('O inverso de {} é {}.'.format(juntar, inverso))
if juntar == inverso:
    print('A frase é um palíndromo.')
else:
    print('A frase não é um palíndromo.')
