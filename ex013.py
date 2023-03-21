preço = float(input('Qual o preço do produto? R$:'))
vista = preço - (preço/100*15)
parcelado = preço + (preço*5/100)
print('o produto de {:.2f} a vista fica {:.2f} parcelado fica {:.2f} '.format(preço, vista, parcelado))
