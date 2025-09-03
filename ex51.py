#Exercício 51 - Progressão Aritmética

p1 = int(input('Digite o primeiro termo:'))
r = int(input('Digite a razão: '))
decimo = p1 + (10-1) * r

for c in range (p1,decimo,r):
    print('{}'.format(c),end=' - ')


