## Crie o jogo Jokenpô

import random
import time

print('\033[1;44m=\033[m' * 40)
print('\033[1;44m+\033[m' * 40)
print('\033[1;44m    J    O    K    E    N    P    Ô     \033[m')
print('\033[1;44m+\033[m' * 40)
print('\033[1;44m=\033[m' * 40)
alternativa = ['PEDRA', 'PAPEL', 'TESOURA']
pc = random.choice(alternativa)
print(' ')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
vc = int(input('Digite qual você escolhe: '))
if vc == 1:
    vc = 'PEDRA'
elif vc == 2:
    vc = 'PAPEL'
elif vc == 3:
    vc = 'TESOURA'
print('=-'*20)
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ')
time.sleep(0.5)
print('=-'*20)
if pc == 'PEDRA' and vc == 'PEDRA' or pc == 'PAPEL' and vc == 'PAPEL' or pc == 'TESOURA' and vc == 'TESOURA':
    print(' ')
    print('\033[1;44mO jogo empatou, pois você escolheu {} e o computador também escolheu {}!!\033[m'.format(vc, pc))
elif pc == 'PEDRA' and vc == 'TESOURA' or pc == 'PAPEL' and vc == 'PEDRA' or pc == 'TESOURA' and vc == 'PAPEL':
    print(' ')
    print('\033[1;41mO computador venceu!! Você escolheu {} e o computador escolheu {}.\033[m'.format(vc, pc))
elif pc == 'PEDRA' and vc == 'PAPEL' or pc == 'PAPEL' and vc == 'TESOURA' or pc == 'TESOURA' and vc == 'PEDRA':
    print(' ')
    print('\033[1;42mParabéns, você venceu!! Você escolheu {} e o computador escolheu {}.\033[m'.format(vc, pc))
else:
    print(' ')
    print('\033[1;41mNão foi possível jogar, você digitou uma jogada inválida!\033[m')