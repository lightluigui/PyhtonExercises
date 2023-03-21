import random

'''print('vou pensar em um numero entre 0 e 5 tente adivinhar...')
chute = int(input('Em que numero pensei? '))
lista = [0,1,2,3,4,5]
escolhido =random.choice(lista)
print('PROSCESSANDO...')
if escolhido == chute:
    print('Parabens Acertou miseravel')
else:
    print('Nao foi dessa vez')'''
#outra forma de fazer tambem pode ser assim:
print('-=-'*15)
print('vou pensar em um numero entre 0 e 5 tente adivinhar...')
print('-=-'*15)
computador = random.randint(0,5)#o randint vai escolher aleatoriamente um numero entre os que estao detro de ()
chute = int(input('Em que numero pensei? '))
if computador == chute:
    print('Parabens Acertou miseravel')
else:
    print('Nao foi dessa vez a resposta certa era {}'.format(computador))

