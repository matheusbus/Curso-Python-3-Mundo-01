## Fórmula matemática (Manual)
#from math import sqrt
#b = float(input('Digite o valor do cateto adjacente: '))
#c = float(input('Digite o valor do cateto oposto: '))
#hyp = b **2 + c**2
#print('A hipotenusa vale {:.0f}.'.format(sqrt(hyp)))

## Utilizando a função Hypot da biblioteca math
#import math
#ca = float(input('Digite o valor do cateto adjacente: '))
#co = float(input('Digite o valor do cateto oposto: '))
#hi = math.hypot(ca, co)
#print('A hipotenusa vale {:.2f}'.format(hi))

## Ou
from math import hypot
ca = float(input('Qual o valor do cateto adjacente: '))
co = float(input('Qual o valor do cateto oposto: '))
hi = hypot(ca, co)
print('A hipotenusa vale {:.2f}'.format(hi))
