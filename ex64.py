#Exercício 63 - Sequência de Fibonacci

n = 0
q = 0
media = 0
maior = None
menor = None
contador = 0
total = 0

while q != 'N':
    n = int(input('Digite vários  números: '))
    q = str(input('Quer continuar? [S/N]: ')).upper()

    contador = contador + 1
    total = total + n
    media = total/contador
    
    if maior == None:
        maior = n
        menor = n

    if n > maior:
        maior = n

    if n < menor:
        menor = n


print('Você digitou {} números e a média foi {}'.format(contador, media))
print('O maior numero foi {} e o menor foi {}'.format(maior, menor))