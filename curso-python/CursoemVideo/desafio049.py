# Refaça o desafio 009, mostrando a tabuada de um número digitado pelo usuário
# só que agora utilizando o laço for.

import time
n = int(input('Digite o número que deseja saber a tabuada: '))
for c in range(1 ,11):
    print('{}  X  {}  =   {}'.format(n, c, n*c))
    time.sleep(0)
