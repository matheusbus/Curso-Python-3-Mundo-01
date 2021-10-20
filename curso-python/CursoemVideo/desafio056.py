# Desenvolva um programa que leia o nome, idade e sexo de QUATRO pessoas.
# No final mostre:
# - A média de idade do grupo;
# - Qual é o nome do homem mais velho;
# - Quantas mulheres tem menos de 20 anos.

np = 1
idades = 0
ihmv = 0
qmm = 0
for c in range(1, 5):
    print('==== {}° PESSOA ===='.format(c))
    nome = str(input('Digite o nome da {}° pessoa: '.format(np))).title()
    idade = int(input('Digite a idade da {}° pessoa: '.format(np)))
    sexo = str(input('Digite o sexo da {}° pessoa [M] ou [F]: '.format(np))).upper()
    np = np + 1
    idades = idades + idade
    if idade > ihmv and sexo == 'M':
        ihmv = idade
        nomemv = nome
    if idade < 20 and sexo == 'F':
        qmm = qmm + 1
mediaidade = idades / np
print()
print('A média de idade do grupo é de {:.0f} anos.'.format(mediaidade))
print()
print('O homem mais velho se chama {}.'.format(nomemv))
print()
if qmm == 1:
    print('Foi registrado um total de {} mulher menor de 20 anos.'.format(qmm))
else:
    print('Foi registrado um total de {} mulheres menores de 20 anos.'.format(qmm))
