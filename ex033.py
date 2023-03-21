dis = float(input('Digite a distancia da viagem:'))
preco = dis*0.5
if dis > 200:
    preco = dis*0.45
print('A Viagem de {} KM deu no valor de {:.2f}R$'.format(dis, preco))
