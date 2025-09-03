#Exercício 40 - Média e Aprovação do Aluno

n1 = float(input('Digite sua primeira nota:  '))
n2 = float(input('Digite sua segunda nota:  '))

m = (n1+n2)/2

if m < 5:
    print('Reprovado')
elif m >= 5 and m <= 6.9:
    print('Recuperação')
elif m >=7:
    print('Aprovado')
