print('======= CONVERSOR DE GRAUS CELSIUS EM FAHRENHEIT =======')
c = float(input('Digite uma temperatura em graus celcius: '))
f = (c * 9 / 5) + 32
print('A temperatura de {}°C equivale a temperatura de {}°F.'.format(c, f))

fa = float(input('Agora digite uma temperatura em graus Fahrenheit: '))
ce = (fa - 32) * 5 / 9
print('A temperatura de {}°F equivale a temperatura de {}°C.'.format(fa, ce))
