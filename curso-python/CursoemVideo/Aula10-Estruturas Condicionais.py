#tempo = int(input('Quantos anos tem o seu carro? '))
#print('Carro novo' if tempo <=3 else 'Carro Velho')
#print('---FIM---')

#nome = str(input('Qual o seu nome: '))
#if nome == 'Matheus' or 'João':
#    print('Que nome lindo! ')
#else:
#    print('Seu nome é tão normal quanto a luz do dia.')
#print('Bom dia, {}!'.format(nome))

##Cálculo da média:

import emoji
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print(emoji.emojize('Parabéns, com a média final {} você foi aprovado :grinning_face: .'.format(media), use_aliases= True))
else:
    print(emoji.emojize('Que decepção, com a média final {:.2f} você foi reprovado :crying_face: .'.format(media), use_aliases= True))
print('---FIM---')
