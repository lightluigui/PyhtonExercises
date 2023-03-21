n1 = float(input('digite um numero'))
n2 = float(input('digite um numero'))
n3 = float(input('digite um numero'))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n2 and n3<n1:
    menor = n3

print(' o menor numero é {}'.format(menor))