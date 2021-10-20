#import math
#ang = float(input('Digite o ângulo de deseja: '))
#rad = math.radians(ang)
#print('O seno de {}° é igual a {:.2f}'.format(ang, math.sin(rad)))
#print('O cosseno de {}° é igaul a {:.2f}'.format(ang, math.cos(rad)))
#print('A tangente de {} é igual a {:.2f}'.format(ang, math.tan(rad)))

## Ou

from math import radians, sin, cos, tan
ang = (float(input('Digite um ângulo: ')))
rad = radians(ang)
seno = sin(rad)
cosseno = cos(rad)
tangente = tan(rad)
print('O seno de {} vale {:.2f}'.format(ang, seno))
print('O cosseno de {} vale {:.2f}'.format(ang, cosseno))
print('A tangente de {} vale {:.2f}'.format(ang, tangente))
