vel = float(input('Qual a velocidade do carro? '))
limite = 80
multa = (vel-80) * 7
if vel > limite:
    print('Multa, você esta muito rapido, tera que pagar {}R$ de multa'.format(multa))
else:
    print('Muito bem, continue assim')
print('Dirija com cuidado')