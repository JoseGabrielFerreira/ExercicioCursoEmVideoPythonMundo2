#Exercício 48 - Soma Ímpares Múltiplos de 3

s = 0
for c in range (1, 500):
    if c %2 == 1 and c%3 == 0:
      s = s + c
print ('O resultado da soma de todos os valores é: {}'.format(s))
