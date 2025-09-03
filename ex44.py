#Exercício 44 - Condições de Pagamento

valor = float(input('PREÇO DAS COMPRAS: R$'))
print(""" QUAL É A FORMA DE PAGAMENTO?
    [1] PARA À VISTA DINHEIRO OU PIX
    [2] PARA À VISTA CARTÃO
    [3] DUAS VEZES NO CARTÃO
    [4] TRÊS VEZES OU MAIS NO CARTÃO""")

opção = int(input('DIGITE A OPÇÃO SELECIONADA:  '))

if opção == 1:
    desc = (valor*10/100) - valor
    print('Sua conta de {} reais vai custar {} reais'.format(valor,desc))
elif opção == 2:
    desc2 = (valor*5/100) - valor
    print('Sua conta de {} reais vai custar {} reais'.format(valor,desc2))
elif opção == 3:
    print('Você terá que pagar {} reais'.format(valor))
elif opção == 4:
    parcelas = int(input('EM QUANTAS PARCELAS?  '))
    juros = parcelas/(valor*20/100) + valor

    print('Sua conta de {} reais vai custar {} reais'.format(valor,juros))
else:
    print('OPÇÃO INVÁLIDA')
