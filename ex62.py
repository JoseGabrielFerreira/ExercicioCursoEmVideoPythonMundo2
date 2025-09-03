#Exercíco 62-  Super Progressão Aritmética v3.0

n = int(input('Digite o primeiro termo da sua p.a: '))
r = int(input('Digite a razão da sua p.a: '))

contador = 0
termo = n
t = 0
total = 0
q = 10

print('Os 10 primeiros termos da P.A. são:')
while q != 0:  
    total = total + q
    while contador <=total:
        termo = termo + r
        contador = contador +1
        print(termo)
    q = int(input('Você quer ver mais quantos termos? '))
