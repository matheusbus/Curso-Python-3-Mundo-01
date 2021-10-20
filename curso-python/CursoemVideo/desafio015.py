print('======= ALUGUEL DE CARROS ======')
diaria = int(input('Por quantos dias o carro foi alugado ? '))
qdiaria = diaria * 60
km = float(input('Quantos kilometros foram rodados ? '))
qkm = km * 0.15
print('O valor total a pagar pelo carro será de R${:.2f}.'.format(qdiaria + qkm))
print('R${:.2f} pelo tanto de dias e R${:.2f} pelo tanto de km rodado.'.format(qdiaria, qkm))
