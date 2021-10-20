##Crie um programa que leia o nome de uma cidade e diga se ela tem "Santo" no nome.

cidade = str(input('Digite o nome de uma cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
