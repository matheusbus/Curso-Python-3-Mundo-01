##Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por Km acima do limite.

kmh = int(input('Qual a velocidade do carro: '))
if kmh >80 :
    multa = (kmh - 80) * 7
    print('Você foi multado em R${:.2f}.'.format(multa))
else:
    print('Velocidade dentro do limite permitido!')
print('Tenha um bom dia, dirija com segurança!')
print('-----FIM-----')
