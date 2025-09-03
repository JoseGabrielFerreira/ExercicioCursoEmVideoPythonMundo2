# #Exercício 36 - Aprovando Empréstimo

valor_casa = float(input('Qual é o valor da casa?  '))
salário = float(input('Qual é o seu salário  '))
anos = int(input('Quantos anos você vai pagar?  '))

conta = float(valor_casa/(anos*12))

if conta > salário*0.30:
     print('Empréstimo negado')
else:
    print('Empréstimo aprovado')
