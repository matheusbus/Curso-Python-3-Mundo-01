##Crie um programa que leia 3 segmentos de reta e diga se é possível formar um triângulo unindo as 3 retas.

r1 = int(input('Digite o valor da reta 1: '))
r2 = int(input('Digite o valor da reta 2: '))
r3 = int(input('Digite o valor da reta 3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os valores {}, {}, {} podem formar um triângulo.'.format(r1, r2, r3))
else:
    print('Os valores {}, {}, {} não podem formar um triângulo.'.format(r1, r2, r3))
print('-----FIM-----')
