import math
co = float(input('comprimeto do cateto oposto '))
ca = float(input('comprimeto do cateto adjacente '))
hi = math.ceil(math.hypot(co, ca))
print('a hipotenusa é {}'.format(hi))





#ceil arredonda numero
#hypot calcula a hipotenusa
#trunc ele pega apenas o valor inteiro de um numero real

#hi = (co ** 2 + ca **2) ** (1/2)
#print('a hipotenusa é {:.2f}'.format(hi))
