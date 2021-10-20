nome = str(input('Qual o seu nome: '))
if nome == 'Matheus':
    print('Que nome lindo!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Gustavo':
    print('Seu nome é bem popular no Brasil!')
elif nome == 'Maria' or nome == 'Ana' or nome == 'Cláudia' or nome == 'Joana' or nome == 'Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome não é tão popular, nem tão raro, ele é normal!')
print('Tenha um bom dia, {}!'.format(nome))
