print('====== DESCONTO DO MÊS ======')
p = float(input('Qual o valor do produto ? R$'))
d = float(input('Qual a porcentagem de desconto ? em % '))
pcd = p - (p * d/100)
des = p - pcd
print('O produto ficará no valor de R${:.2f} . O valor total do desconto será de R${:.2f}.'.format(pcd, des))
