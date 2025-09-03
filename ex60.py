#Exercício 60 -Cálculo do Fatorial

n = int(input('Digite um número para ser fatorado: '))
resultado = 1
contador = n

while contador > 0:
    resultado = resultado * contador
    contador = contador -1
print(resultado)


