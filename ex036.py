salario = float(input('Digite seu Salario:'))
if salario <=1250 :
     novo = salario +(salario * 15 / 100)
else:
     novo = salario +(salario * 10 / 100)

print('o salario de {} aumentou para {}'.format(salario,novo))