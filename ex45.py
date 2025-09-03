#Exercício 45 - Pedra, Papel e Tesoura

import random

print(""":
[1] PARA PEDRA
[2] PARA PAPEL
[3] PARA TESOURA""")
opção = int(input('Selecione uma opção:  '))

if opção == 1:
    print('Muito bem, você escolheu PEDRA')
elif opção == 2:
    print('Muito bem, você escolheu PAPEL')
elif opção == 3:
    print ('Muito bem, você escolheu TESOURA')
print('                                            ')
print('Agora vamos ver qual opção seu oponente escolheu: ')
print('                                            ')

pedra = str('PEDRA')
papel = str('PAPEL')
tesoura = str('TESOURA')

jogo = [pedra,papel,tesoura]
adversário = random.choice(jogo)
print('Seu oponente escolheu {}'.format(adversário))

print('                                  ')

if opção == 1 and adversário == tesoura:
     print('Párabens, você venceu!')
elif opção == 2 and adversário == pedra:
    print('Parabéns, você venceu!')
elif opção == 3 and adversário == papel:
    print('Parabéns, você venceu!')
elif opção == 1 and adversário == pedra or opção == 2 and adversário == papel or opção == 3 and adversário == tesoura:
     print('Empate, joguem denovo')
else:
     print('Você perdeu')



