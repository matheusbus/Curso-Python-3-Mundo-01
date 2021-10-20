## Fatiamento de strings

#Exemplo 1 (imprimir 9a casa)
#frase = 'Curso em Vídeo Python'
#print(frase[9])

#Exemplo 2 (imprimir da casa 9 até a casa 12)
#frase = 'Curso em Vídeo Python'
#print(frase[9:13])

#Exemplo 3 (imprimir da casa 9 até a 20 saltando de 2 em 2 casas)
#frase = 'Curso em Vídeo Python'
#print(frase[9:21:2])

#Exemplo 4 (omitir o ínicio: pega o ínicio até a casa desejada)
#frase = 'Curso em Vídeo Python'
#print(frase[:5])

#Exemplo 5 (omitir o final: pega a desejada casa até o final)
#frase = 'Curso em vídeo Python'
#print(frase[15:])


## Análise de strings

#Exemplo 1 (comprimento da frase: len (lenght))
#frase = 'Curso em Vídeo Python'
#print(len(frase))

#Exemplo 2 (contar quantas vezes aparece tal caractere, dif minúsculo de maiúsculo)
#frase = 'Curso em vídeo Python'
#print(frase.count('o'))

#Exemplo 3 (contar quantas vezes aparece tal caractere, dif minúsculo de maiúsculo, com fatiamento)
#frase = 'Curso em Vídeo Python'
#print(frase.count('o',0,13))
#print(frase.count('o',0,14))

#Exemplo 4 (procurar um caractere ou um conjunto de caracteres na string: vai indicar que posição se inicia)
#frase = 'Curso em Vídeo Python'
#print(frase.find('deo'))

#Exemplo 5 (procurar uma string que não existe, irá retornar o valor -1, que não existe)
#frase = 'Curso em Vídeo Python'
#print(frase.find('Android'))

#Exemplo 6 (Existe a palavra tal na string?: retorna verdadeiro ou falso!)
#frase = 'Curso em Vídeo Python'
#print('Android' in frase)

##Transformação de Strings

#Exemplo 7 (Replace: substitui algo na string)
#frase = 'Curso em vídeo Python'
#print(frase.replace('Python', 'Android'))

#Exemplo 8 (Upper(): colocar tudo em letras maiúsculas)
#frase = 'Matheus Buschermoehle'
#print(frase.upper())

#Exemplo 9 (Lower(): colocar tudo em letras minúsculas)
#frase = 'MATHEUS BUSCHERMOEHLE'
#print(frase.lower())

#Exemplo 10  (Capitalize(): colocar tudo em minúsculo deixando somente a primeira letra maiúscula)
#frase = 'MATHEUS BUSCHERMOEHLE'
#print(frase.capitalize())

#Exemplo 11 (Title(): análise de quantas palavras, pelo espaço e transforma a primeira letra de cada palavra em Maiúsc.)
#frase = 'Aprendendo python em curso em vídeo'
#print(frase.title())

#Exemplo 12 (Strip(): remove todos os espaços inúteis no início e no fim da string)
#           (rStrip(): remove todos os espaços inúteis na DIREITA da string)
#           (lStrip(): remove todos os espaços inúteis na ESQUERDA da string)
#frase = '  Aprendendo Python  '
#print(frase.strip())

##Divisão
#Exemplo 13 (Split(): divide os blocos de espaços da string, ele gera uma lista por palavra )
#frase = 'Curso em vídeo '
#print(frase.split())

##Junção
#Exemplo 14 (Join(): junta os elementos de frase da string)
#frase = 'Curso em vídeo Python'
#print('-'.join(frase))
