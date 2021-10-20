# Desenvolva uma lógica que leia o peso e altura de uma pessoa e calcule o seu IMC, e mostre na tela de acordo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: peso ideal
# Entre 25 até 30: Sobrepeso
# Entre 30 e 40: Obesidade
# Acima de 40: Obesidade Mórbida

print('\033[1;41m=-\033[m' * 19)
print('\033[1;41m  CÁLCULO DE INDICE DE MASSA CORPORAL \033[m')
print(19 * '\033[1;41m=-\033[m')
altura = float(input('Digite a sua altura em m: '))
peso = float(input('Digite seu peso em kgs: '))
imc = peso / (altura **2)
if imc < 18.5:
    print('\033[1;41mSeu Imc é {:.1f}! Você está abaixo do peso.\033[m'.format(imc))
elif 25 >= imc >= 18.5:
    print('\033[1;42mSeu Imc é {:.1f}! Você está no seu peso ideal.\033[m'.format(imc))
elif 30 >= imc > 25:
    print('\033[1;41mSeu Imc é {:.1f}! Você está com sobrepeso.\033[m'.format(imc))
elif 40 >= imc > 30:
    print('\033[1;41mSeu Imc é {:.1f}! Você está com Obesidade.\033[m'.format(imc))
elif imc > 40:
    print('\033[1;41mSeu Imc é {:.1f}! Você está com obesidade mórbida.\033[m'.format(imc))
