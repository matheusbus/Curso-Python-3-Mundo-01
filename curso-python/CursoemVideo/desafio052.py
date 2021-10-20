# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

print('\033[46mº\033[m'*30)
print('\033[46mº N Ú M E R O S  P R I M O S º\033[m')
print('\033[46mº\033[m'*30)

tot = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[32m{}\033[m '.format(c), end='')
        tot += 1
    else:
        print('\033[31m{}\033[m '.format(c), end='')
print()
print('O número {} foi divisível {} vezes.'.format(n, tot))
if tot == 2:
    print('\033[32mO número digitado é primo.\033[m')
else:
    print('\033[31mO número digitado NÃO é primo.\033[m')
