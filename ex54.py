#Exercício 54 - Grupo da Maioridade

from datetime import date
ano_atual = date.today().year
menores = 0
maiores = 0
for c in range (1,8):
    c = int(input('Digite o ano do nascimento da {}ª pessoa: '.format(c)))

    idade = ano_atual- c

    if idade < 18:

        menores +=1

    else:

         maiores +=1

print('Temos {} menores  e {} maiores'.format(menores,maiores))