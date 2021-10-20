##Crie um programa que leia a distância de uma viagem, se ela for de até 200km, cobre R$0,50 por km, se for
##mais longa, cobre R$0,45 por km.

print('Cálculo do valor da viagem')
dist = int(input('Qual a distância da viagem: '))
if dist <= 200:
    valor = dist * 0.50
    print('O valor da viagem será de R${:.2f}.'.format(valor))
else:
    valor = dist * 0.45
    print('O valor da viagem será de R${:.2f}'.format(valor))
print('.......Fim.......')
