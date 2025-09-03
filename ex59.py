#Exercício 59 - Criando um Menu de Opções

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

somar = 0
multiplicar = 0
maior = 0
novos_numeros = 0
menu = 0


while menu != 5:
    menu = int(input("""
                    [1] SOMAR
                    [2] MULTIPLICAR
                    [3] MAIOR
                    [4] NOVOS NÚMEROS
                    [5] SAIR DO PROGRAMA 
                    """))
    if menu == 1:
        somar =  n1 + n2
        print(somar)
        break
    elif menu == 2:
        multiplicar = n1*n2
        print(multiplicar)
        break
    elif menu == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2,n1))
        else:
            print('{} e {} são iguais'.format(n1,n2))

            break
    elif menu == 4:
        n1 = int(input('DIGITE UM NOVO NÚMERO: '))
        n2 = int(input('DIGITE OUTRO NÚMERO NOVO: '))
        
    elif menu == 5:
        print("Encerrando o programa...")
    else:
        print('Opção inválida, tente novamente')
