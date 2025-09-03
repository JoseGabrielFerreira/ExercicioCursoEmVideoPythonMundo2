#Exercício 56 - Analisador Completo

total = 0
homem_velho = 0
totalmulher = 0
nome_homem_velho = 0

for i in range(1, 5):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    genero = str(input('Digite seu gênero: ')).upper()
    print('-'*35)

    total = total + idade

    if i == 1 and genero == 'HOMEM':
        homem_velho = idade
        nome_homem_velho = nome
    if genero in 'HOMEM' and idade > homem_velho:
        homem_velho = idade
        nome_homem_velho = nome
    if genero in 'MULHER' and idade < 20:
        totalmulher = totalmulher + 1



def calculo(total):
    media = total/4
    return (media)  

resultado = calculo(total)
print('A média de idade das pessoas são {}'.format(resultado))
print('O nome do homem mais velho é {} e ele tem {} anos'.format(nome_homem_velho,homem_velho))
print('Temos {} mulheres maiores de 20 anos'.format(totalmulher))