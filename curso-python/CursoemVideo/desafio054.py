# Crie um programa que leia o ano de nascimento de SETE PESSOAS. No final, mostre quantas pessoas
# já são maiores e quantas ainda não atingiram a maioridade.

import datetime

aa = datetime.date.today().year
p = 1
m = 0
nm = 0
qtd = int(input('De quantas pessoas você deseja saber a maioridade: '))
for a in range(0, qtd):
    ano = int(input('Digite o ano de nascimento da {}° pessoa: '.format(p)))
    p = p + 1
    if aa - ano >= 21:
        m = m + 1
    else:
        nm = nm + 1
print('{} dessas pessoas são maiores de 21 anos de idade.'.format(m))
print('{} dessas pessoas não são maiores de 21 anos de idade.'.format(nm))
