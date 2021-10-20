# Crie um programa que faça a contagem regressiva para o estouro de fogos de artifícios,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles

import time

for c in range(1000, -1, -1):
    print(c)
    time.sleep(1)
print('Feliz Ano Novo!!!')
