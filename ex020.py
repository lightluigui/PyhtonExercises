import random

a1 = input('nome do primeiro :')
a2 = input('o nome do segundo :')
a3 = input('nome do terceiro :')
a4 = input('nome do quarto :')

lista = [a1, a2, a3, a4]
ordem = random.shuffle(lista)
print('os intregrantes do trabalho sao {}'.format(lista))

#shuffle embaralha a ordem dos intens
