#Exercício 43 - IMC - Índice de Massa Corporal

p = float(input('Digite seu peso:  '))
a = float(input('Digite sua altura:  '))

imc = p/(a**2)

if imc <= 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <=25:
    print('Peso ideal')
elif imc >=25 and imc <=30:
    print('Sobrepeso')
elif imc >=30 and imc <=40:
    print('Obesidade')
else:
     print('Obesidade Mórbida')
