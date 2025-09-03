#Exercício 37 - Conversão de Bases Numéricas

n = int(input('Digite um numero inteiro: '))
print("""[1] PARA CONVERTER EM BINÁRIO
[2] PARA CONVERTER EM OCTAL
[3] PARA CONVERTER EM HEXADECIMAL""")
opção = int(input('Selecione uma opção: '))

if opção == 1:
        print(bin(n)[2:])
elif opção == 2:
    print(oct(n))
elif opção == 3:
    print(hex(n))
else:
    print('OPÇÂO INVÁLIDA')

