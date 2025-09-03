#Exercício 58 - Jogo da Adivinhação v2.0

from random import randint
from time import sleep

computador = randint(1,10)
tentativas = 0

n = int (input('TENTE ADIVINHAR O NÚMERO QUE ESTOU PENSANDO: '))
tentativas = tentativas + 1
print('-'*35)
print('PROCESSANDO...')
sleep(3)

while n != computador:
    print('VOCÊ ERROU,TENTE DE NOVO')
    print('-'*35)
    n = int (input('DIGITE OUTRO NÚMERO: '))
    print('-'*35)
    tentativas = tentativas + 1
if n == computador:
    print('PARABÉNS, VOCÊ ACERTOU!!')
print('VOCÊ TENTOU ACERTAR O NÚMERO QUE PENSEI {} VEZES'.format(tentativas))
