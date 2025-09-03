#Exercício 42 - Tipos de Triângulos

m1 = float(input('Digite a medida da primeira reta: '))
m2 = float(input('Digite a medida da segunda reta: '))
m3 = float(input('Digite a medida da terceira reta: '))

if (m1 + m2 > m3) and (m2 + m3 > m1) and (m1 + m3 > m2):
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')

if m1 == m2 and m1 == m3:
    print('E é um Triângulo equilatero')
elif m1 == m2 and m1 != m3 or m1 == m3 and m1 != m2:
    print('E é um Triângulo isóceles')
elif m1 != m2 != m3 and (m1 + m2 < m3) and (m2 + m3 < m1) and (m1 + m3 < m2):
    print('E é um Triângulo escaleno')
