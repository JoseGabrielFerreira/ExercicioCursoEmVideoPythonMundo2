# Exercício 67 – Tabuada v3.0

n = 0
s = 0
n = int(input('Quer ver a tabuada de qual valor? '))

while n > 0:
    s = s + 1
    print(f'{n} x {s} = {n*s}')
    if s == 10:
     break
