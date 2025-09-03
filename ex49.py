#Exercício 49 - Tabuada

n = int(input('Digite um número: '))
print('A tabuada de {} é:'.format(n))
for c in range (1,11):
    print('{}  X  {} é = {}'.format(n,c,n*c))