#Exercício 39 - Alistamento Militar

from datetime import date
ano_atual = date.today().year

ano = int(input('Digite o ano do seu nascimento:  '))

idade = ano_atual - ano
tempo = 18 - idade

if idade >18 :
    print('Já passou o tempo de se alistar')
elif idade == 18:
     print('É a hora de se alistar')
elif idade <18:
    print('Você ainda vai se alistar, falta {} anos para voce se alistar'.format(tempo))
