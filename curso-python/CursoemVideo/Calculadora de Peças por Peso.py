import math
pesp = float(input('Digite o peso específico do parafuso em g: '))
ptot = float(input('Digite o peso total dos parafusos em g: '))
qtd = ptot / pesp
print('Quantidade de peças: {}'.format(math.floor(qtd)))
