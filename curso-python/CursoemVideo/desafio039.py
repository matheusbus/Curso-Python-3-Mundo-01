## Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

from datetime import date

anoatual = date.today().year
ano = int(input('Qual o ano do seu nascimento: '))
idade = anoatual - ano
print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, anoatual))
if idade == 18:
    print('Você possui {} anos. É hora de se alistar.'.format(idade))
    print('Seu alistamento será no ano de {}.'.format(anoatual))
elif idade < 18:
    prazo = 18 - idade
    if prazo == 1:
        print('Você possui {} anos, falta {} ano para poder se alistar.'.format(idade, prazo))
    else:
        print('Você possui {} anos, faltam {} anos para poder se alistar.'.format(idade, prazo))
    print('Seu alistamento será em {}.'.format(anoatual + prazo))
elif idade > 18:
    prazo = idade - 18
    if prazo == 1:
        print('Você possui {} anos, já passou {} ano da hora de se alistar.'.format(idade, prazo))
    else:
        print('Você possui {} anos, já passou {} anos da hora de se alistar.'.format(idade, prazo))
    print('Seu alistamento foi em {}.'.format(anoatual - prazo))
