# Exercício 69 – Análise de dados do grupo

contaridade = 0
contarhomem = 0
mulhermenor = 0

while True:
    idade = int(input('IDADE: '))
    sexo = str(input('H/M : ')).upper()
    continuar = str(input('S/N: ')).upper() 

    if idade > 18:
        contaridade = contaridade +1
    if sexo == 'H':
         contarhomem = contarhomem + 1
    if sexo == 'M' and idade < 20:
        mulhermenor = mulhermenor + 1

    if continuar == 'N':
        break
print(f'Temos {contaridade} pessoas cadastrasdas maiores de 18 anos. ')
print(f'Foram cadastrados {contarhomem} homens. ')
print(f'Foram cadastrados {mulhermenor} mulheres abaixo de 20 anos. ')