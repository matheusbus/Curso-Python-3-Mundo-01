##Crie um programa que leia 3 números e mostre o maior e o menor.

n1 = int(input('Digie o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    maior = n1
    print('O maior valor digitado foi {}.'.format(maior))
else:
    if n2 > n1 and n2 > n3:
        maior = n2
        print('O maior valor digitado foi {}.'.format(maior))
    else:
        maior = n3
        print('O maior valor digitado foi {}.'.format(maior))

if n1 < n2 and n1 < n3:
    menor = n1
    print('O menor valor digitado foi {}.'.format(menor))
else:
    if n2 < n1 and n2 < n3:
        menor = n2
        print('O menor valor digitado foi {}.'.format(menor))
    else:
        menor = n3
        print('O menor valor digitado foi {}.'.format(menor))
print('-----FIM-----')
