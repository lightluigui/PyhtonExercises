import random

a1 = input('nome do aluno um:')
a2 = input('o nome do segundo aluno:')
a3 = input('nome do terceiro aluno:')
a4 = input('nome do quarto aluno:')

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {} '.format(escolhido))


#para o python um lista de objetos fica entre colchetes
#random.choice vai escolher um item deto daquela lista

