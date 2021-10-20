## Crie um programa que leia tres retas e diga se elas podem formar um triangulo.
## Diga também se ele é:
## Equilátero: todos os lados iguais.
## Isósceles: dois lados iguais.
## Escaleno: todos os lados diferentes.

print('\033[1;46m=-\033[m'*20)
print('\033[1;41m  CRIAÇÃO E CLASSIFICAÇÃO DE TRIÂNGULOS \033[m')
print('\033[1;46m=-\033[m'*20)
r1 = int(input('Digite o comprimento do primeiro lado: '))
r2 = int(input('Digite o comprimento do segundo lado: '))
r3 = int(input('Digite o comprimento do terceiro lado: '))
if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('Os valores {}, {} e {} \033[1;42mPODEM\033[m formar um triângulo.'.format(r1, r2, r3))
    if r1 == r2 == r3:
        print('O triângulo a ser formado é \033[1;46mEquilátero\033[m.')
    elif r1 == r2 or r2 == r3 or r1 == r3:
        print('O triângulo a ser formado é \033[1;46mIsósceles\033[m.')
    elif r1 != r2 != r3 != r1:
        print('O triângulo a ser formado é \033[1;46mEscaleno\033[m.')
else:
    print('Os valores {}, {} e {} \033[1;41mNÃO PODEM\033[m formar um triângulo.'.format(r1, r2, r3))
