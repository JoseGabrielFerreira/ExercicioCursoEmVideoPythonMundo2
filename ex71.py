# Exercício 71 - Simulador de caixa eletrônico

valor = int(input("Quanto você quer sacar? R$"))
cedulas = 0

while valor > 0:
        for cedulas in (50,20,10,1):
                resultado = valor//cedulas
                valor %= cedulas

                print (f'Você precisa de {resultado} cédulas de {cedulas} necessárias')
