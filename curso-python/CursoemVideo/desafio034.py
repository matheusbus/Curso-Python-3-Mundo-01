##Crie um programa que leia o salário do funcionário e calcule o valor de um aumento
##Para salários superiores a R$1.250,00 calcule um aumento de 10%
##Para salários inferiores, calcule um aumento de 15%

sal = float(input('Digite o valor do seu salário: R$'))
if sal > 1250:
    nsal = sal + (sal * 10 / 100)
    print('Seu novo salário será de R${:.2f}.'.format(nsal))
    print('Você recebeu um aumento de 10%')
else:
    nsal = sal + (sal * 15 / 100)
    print('Seu novo salário será de R${:.2f}.'.format(nsal))
    print('Você recebeu um aumento de 15%.')
