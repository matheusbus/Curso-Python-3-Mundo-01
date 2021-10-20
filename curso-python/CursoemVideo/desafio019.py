import random
aluno1 = str(input('Digite o nome do 1o aluno: '))
aluno2 = str(input('Digite o nome do 2o aluno: '))
aluno3 = str(input('Digite o nome do 3o aluno: '))
aluno4 = str(input('Digite o nome do 4o aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno sorteado foi {}.'.format(escolhido))
