# Classificação da categoria do atleta de acordo com a idade
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JUNIOR
# Até 30 anos: SÊNIOR
# Acima de 30 anos: MASTER

print('=-'*40)
print('                 Saiba sua categoria de acordo com sua idade')
print('=-'*40)
nome = str(input('Qual o seu nome, querido atleta: ')).title()
idade = int(input('Seja bem-vindo, {}. Digite sua idade: '.format(nome)))
if idade < 9:
    print('Você está na categoria MIRIM, {}.'.format(nome))
elif 14 > idade >= 9:
    print('Você está na categoria INFANTIL, {}.'.format(nome))
elif 19 > idade >= 14:
    print('Você está na categoria JUNIOR, {}.'.format(nome))
elif 30 > idade >= 19:
    print('Você está na categoria SÊNIOR, {}.'.format(nome))
else:
    print('Você está na categoria MASTER, {}.'.format(nome))
