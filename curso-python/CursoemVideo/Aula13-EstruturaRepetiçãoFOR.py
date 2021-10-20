#Nesta aula aprenderemos sobre laços

## Laço C no intervalo(1,10) --> adicionamos parametros a e b no intervalo, para termos o início e fim do laço

# No Python, fazemos    for C in range(1,10):      range = intervalo em inglês
#                           passo
#                       pega

#Prática: escrever varios oi.

#print('oi')
#print('oi')
#print('oi')

#Utilizando estrutura de repetição for:

#Exemplo 1: escrever Oi 5 vezes:
#for C in range(0,5):
#    print('OI')
#print('Fim')

#A estrutura não considera o último número adicionado como parâmetro.

#Exemplo 2: contagem progressiva do 0 ao 5:
#for C in range(0,6):      #Observa-se que para contarmos até o 5, utilizamos o 6 como parâmetro final.
#   print(C)

#Exemplo 3: contagem regressiva do 5 ao 0:
#for C in range(5, -1, -1):       #Note-se que adicionamos o -1 como novo parâmetro.
#   print(C)

#Exemplo 4: pedindo ao usuário um número para ser feita a contagem:
#n = int(input('Digite um número: '))
#for c in range(0, n):
#    print(c)
#print('Fim')
#Perceba que o programa conta até 1 número antes do N, pois o N ele desconsidera.
#Para arrumarmos isso podemos fazer:

#n = int(input('Digite um número: '))
#for c in range(0, n+1):
#    print(c)
#print('Fim')

#Exemplo 5: pedir ao usuário para digitar o início, fim, e o passo:
#i = int(input('Digite o início da contagem: '))
#f = int(input('Digite o fim da contagem: '))
#p = int(input('Digite o passo da contagem: '))
#for c in range(i, f+1, p):
#    print(c)
#print('Fim')

#Exemplo 6: pedir ao usuário para digitar vários números e fazer a soma entre eles:
#s = 0
#for c in range(0,5):
#    n = int(input('Digite um valor: '))
#    s = s + n
#print('A soma de todos os valores é igual a {}.'.format(s))
