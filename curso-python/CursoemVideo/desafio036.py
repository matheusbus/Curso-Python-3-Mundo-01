##Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor
##da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da parcela sabendo que ela não pode
##exceder 30% do salário ou então o empréstimo será negado.

vcasa = float(input('Qual o valor da casa: R$'))
sal = float(input('Qual o seu salário: R$'))
temp = int(input('Em quantos anos deseja pagar: '))
vpar = vcasa / (temp * 12)  ## Cálculo do valor da parcela
sal30 = sal * 30 / 100  ## Cálculo de 30% do salário
if vpar > sal30:
    print('Empréstimo negado, o valor da parcela é de R${:.2f} e ultrapassa 30% do seu sálario.'.format(vpar))
else:
    print('O valor da parcela será de R${:.2f}, empréstimo concedido.'.format(vpar))
