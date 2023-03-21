salario = float(input('Qual o salario do funcionario? R$:'))
aumento = salario + (salario/100*15)
print('o salario de {:.2f} com um aumento de 15% foi para {:.2f}'.format(salario, aumento))
