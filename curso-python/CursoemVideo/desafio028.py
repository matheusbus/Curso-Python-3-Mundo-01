##Crie um programa que faça o computador 'pensar' em um número entre 0 e 5 e peça para o usuário descobrir o número
##sorteado, escreva se acertou ou errou.

#Minha resolução:
#import random

#n1 = random.randint(0, 5)
#n2 = int(input('Adivinhe o número que o computador sorteou, entre 0 e 5: '))
#if n2 == n1:
#    print('Parabéns, você acertou, o número sorteado foi {}.'.format(n1))
#else:
#    print('Você errou, o número sorteado foi {}.'.format(n1))
#print('-----FIM-----')

#Resolução do professor:

from random import randint
from time import sleep

n1 = randint(0, 5)
print('-=-' * 20)
n2 = int(input('Advinhe o número: '))
print('-=-' * 20)
print('Processando...')
sleep(2)
if n2 == n1:
    print('Parabéns, você acertou, o número sorteado foi {}'.format(n1))
else:
    print('Você errou, o número sorteado foi {}'.format(n1))
