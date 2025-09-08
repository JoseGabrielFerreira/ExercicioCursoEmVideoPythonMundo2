# Exercício 70 - Estatísticas em produtos
s = 0
maisdemil = 0
nome_barato = ""
barato = 0
contador  = 0

while True:
    produto = str(input('PRODUTO: '))
    preço = int(input('PREÇO DO PRODUTO: R$'))
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('RESPOSTA: [S/N]  ')).strip().upper()
    s = s + preço
    print(s)

    if preço > 1000:
        maisdemil = maisdemil + 1

    if contador == 0:
        barato = preço
        nome_barato = produto

    if preço < barato: 
        barato = preço
        nome_barato = produto
       
    contador = contador+1

    if resposta == 'N':
        break
    
print(f'O total gasto foi de {s}')
print(f'Temos {maisdemil} produtos acima de Mil reais')
print(f'O produto mais barato é {nome_barato} com o preço de ${barato}')


