# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:

# Média abaixo de 5.0 = reprovado; Média entre 5.0 e 6.9: recuperação; Média 7.0 ou maior: aprovado.

print('=-'*35)
print('      Calcule a sua média e saiba se você passou de ano !!!')
print('=-'*35)
nome = str(input('Olá querido aluno, qual o seu nome: '))
n1 = float(input('Digite sua primeira nota, {}:'.format(nome)))
n2 = float(input('Digite sua segunda nota, {}:'.format(nome)))
media = (n1 + n2) / 2
if media >= 7.0:
    print('Com uma média {:.1f}, você foi aprovado. Parabéns {}!'.format(media, nome))
elif 7.0 > media >= 5.0:
    print('Com uma média {:.1f}, você ficou em recuperação, estude um pouco mais, {}!'.format(media, nome))
else:
    print('Com uma média {:.1f}, você foi reprovado, tente novamente no próximo ano, {}!'.format(media, nome))
