from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raíz quadrada de {} é igual a {:.1f}.'.format(num, floor(raiz)))
