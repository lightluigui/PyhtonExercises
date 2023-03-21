dias=int(input('quantos dias o carro foi alugado? '))
km=float(input('Quantos quilometros foram rodados? '))
pdia = dias*60
pkm = km*0.15
ptotal = pdia+pkm
print('O carro alugado por {} dias, que rodou {} KM, o preço do aluguel vai ser {:.2f} R$'.format(dias, km, ptotal))