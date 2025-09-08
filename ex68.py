# Exercício 68 – Par ou impar

import random 
contador = 0 

while True:
    n = int(input('Diga um valor: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper()

    computador = random.randint(0,10)
    soma =  n + computador

    print(f'O computador escolheu {computador}')
    print(f'A soma entre {computador} e {n} = {soma}')

    if escolha == 'P' and soma %2 == 0:
        contador = contador + 1
        print('Voce venceu')
    else:
        print(f'GAME OVER! Você venceu {contador} vezes.')
        break


