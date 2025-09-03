#Exercício 41 - Classificação de Atletas

from datetime import date
ano_atual = date.today().year

ano = int(input('Digite o ano de seu nascimento:  '))

idade = ano_atual - ano

if idade <=9:
    print('Mirim')
elif idade <=14:
    print('Infantil')
elif idade <=19:
    print('Júnior')
elif idade <=20:
    print('Senior')
else:
    print('Master')

