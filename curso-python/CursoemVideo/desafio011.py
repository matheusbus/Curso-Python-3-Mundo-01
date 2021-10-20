print('======== QUANTIDADE DE TINTA ========')
m1 = float(input('Qual a largura da parede em metros ? '))
m2 = float(input('Qual a altura da parede em metros ? '))
area = m1 * m2
tinta = area / 2
print('A área da parede é de {:.2f}m². Considerando que para cada 2m² se usa 1 litro de tinta, serão utilizados {:.2f} litros.'.format(area, tinta))
