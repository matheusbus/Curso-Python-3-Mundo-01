# Estrutura While - Enquanto

# Utilizando como exemplo o boneco guanabara, que parte em busca da maçã,
# passa por um caminho onde deve avaliar se tem chão, se deve dar um passo,
# um pulo, ou uma moeda.
#
#               O
#              /|\   *         *
# Exemplo 1 -  /|\ __  __  ____  ____ _ maçã
# While não maçã
#   if tem chão
#       passo
#   if tem buraco
#       pula
#   if tem moeda
#       pega
# Pegue maçã


#c = 1
#while c <= 50:
#    print(c)
#    c = c + 1
#print('Fim')

totp = 0
toti = 0
r = "Sim"
while r == "Sim":
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar? [Sim/Não]: ')).title()
    if n % 2 == 0:
        totp = totp + 1
    else:
        toti = toti + 1
print('Ao todo foram digitados {} números pares.'.format(totp))
print("Ao todo foram digitados {} números ímpares.".format(toti))
print('Fim')