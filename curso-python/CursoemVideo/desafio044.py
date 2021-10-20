## Faça um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pgto:
## à vista no dinheiro/cheque: 10% desconto
## à vista no cartão: 5% desconto
## em até 2x no cartão: preço normal
## 3x ou mais no cartão: 20% de juros

print('\033[1;42m$'*40, '\033[m')
print('\033[1;43m   Seja bem-vindo ao supermercado !!     \033[m')
print('\033[1;42m$'*40, '\033[m')
valor = float(input('Qual o valor do produto que deseja levar: R$'))
print('\033[1;41mOk, veja agora as formas de pagamento:\033[m')
print('[ 1 ] À VISTA DINHEIRO/CHEQUE: 10% desconto')
print('[ 2 ] À VISTA NO CARTÃO: 5% desconto')
print('[ 3 ] ATÉ 2x NO CARTÃO: preço normal')
print('[ 4 ] 3x OU MAIS NO CARTÃO: 20% de juros.')
forma = int(input('Digite o número referente a sua forma de pagamento: '))
if forma == 1:
    valordesc = valor - (valor*10/100)
    print('\033[1;42mA forma digitada foi À VISTA DINHEIRO/CHEQUE. O valor do produto passa de R${:.2f} para R${:.2f}!\033[m'.format(valor, valordesc))
elif forma == 2:
    valordesc = valor - (valor*5/100)
    print('\033[1;42mA forma digitada foi À VISTA NO CARTÃO. O valor do produto passa de R${:.2f} para {:.2f}!\033[m'.format(valor, valordesc))
elif forma == 3:
    valordesc = valor
    print('\033[1;44mA forma digitada foi ATÉ 2x NO CARTÃO. O valor ficará igual, R${:.2f}!\033[m'.format(valordesc))
    parcela = valor / 2
    print('\033[1;44mSua compra será parcelada em duas vezes de R${:.2f}.\033[m'.format(parcela))
elif forma == 4:
    valordesc = valor + (valor*20/100)
    print('\033[1;41mA forma digitada foi 3x OU MAIS NO CARTÃO. O valor passa de {:.2f} para {:.2f}!\033[m'.format(valor, valordesc))
    totp = int(input('Em quantas vezes deseja parcelar? '))
    vpar = valordesc / totp
    print('\033[1;41mSua compra será parcelada em {} vezes de R${:.2f}. Totalizando R${:.2f}\033[m'.format(totp, vpar, valordesc))
else:
    print('\033[1;41mOpção de pagamento inválida, tente novamente.\033[m')
