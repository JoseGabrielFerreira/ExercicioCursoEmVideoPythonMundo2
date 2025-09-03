#Exercício 57 - Validação de dados

sexo = str(input('Digite seu sexo [M/F]: ')).upper()
while sexo not in ['M' or 'F']:
    print('Tente novamente')
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
print('Sexo registrado com sucesso:', sexo)
