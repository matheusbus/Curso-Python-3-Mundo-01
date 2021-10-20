print('======= AUMENTO DE SALÁRIO EM 15% =======')
sal = float(input('Qual o seu salário atual ? R$'))
nsal = sal + (sal * 15/100)
print('Seu novo salário será de R${:.2f} . O total do aumento é de R${:.2f}.'.format(nsal, nsal - sal))
