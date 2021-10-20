##Faça um programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome.

nome = str(input('Qual o seu nome completo: ')).strip().split()
print('Prazer em te conhecer!')
print('O seu primeiro nome é {}.'.format(nome[0]))
print('O seu último nome é {}.'.format(nome[len(nome)-1]))
