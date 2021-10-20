##Cores, estilos e bakground
#Style 0 = Nada, 1 = Negrito, 4 = Sublinhado, 7 = Inverter cores
#Text 30 = Branco, 31 = red, 32 = verde, 33 = amarelo = 34 = azul, 35 = violeta, 36 = azul claro, 37 = cinza
#Background = 40 = Branco, 41 = red, 42 = verde, 43 = amarelo = 44 = azul, 45 = violeta, 46 = azul claro, 47 = cinza
##Fórmula = print('\033[1;31;43mtexto')

print('\033[7;33;44mOlá, Mundo!\033[m')

a = '//////'
b = '//////'
c = '//////'
print('Os valores são \033[32m{}\033[m \033[31m{}\033[m {}'.format(a, b, c))

print(len('Prova de Python'))
