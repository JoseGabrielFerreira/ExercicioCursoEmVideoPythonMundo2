#Exercíco 61- Progressão Aritmética v2.0
n = int(input('Digite o primeiro termo da sua p.a: '))
r = int(input('Digite a razão da sua p.a: '))

contador = 0
termo = n


print('Os 10 primeiros termos da P.A. são:')

while contador <10:
    termo = termo + r
    contador = contador +1
    print(termo)
