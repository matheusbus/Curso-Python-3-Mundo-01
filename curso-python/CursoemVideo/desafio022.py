##Crie um programa que leia o nome de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas;
# - O nome com todas as letras minúsculas;
# - Quantas letras tem o nome (sem considerar espaços)
# - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando seu nome...')
print('O nome em letras maiúsculas: {}'.format(nome.upper()))
print('O nome em letras minúsculas: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele possui {} letras.'.format(separa[0], len(separa[0])))
