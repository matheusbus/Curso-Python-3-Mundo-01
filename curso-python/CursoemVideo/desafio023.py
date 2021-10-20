##Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digítos separados.

#import random

#num = str(random.randint(0,9999))
#print('Número gerado: {}.'.format(num))
#print('Unidade: {}.'.format(num[3]))
#print('Dezena: {}.'.format(num[2]))
#print('Centena: {}.'.format(num[1]))
#print('Uni. Milhar: {}.'.format(num[0]))

num = int(input('Digite um número entra 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("Analisando número...")
print('Unidade: {}.'.format(u))
print('Dezana: {}.'.format(d))
print('Centena: {}.'.format(c))
print('Milhar: {}.'.format(m))
