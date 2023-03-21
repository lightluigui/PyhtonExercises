import random
tentativas = 0
computador = random.randint(0,10)
print('Sou seu pc imbecil advinha o numero que eu pensei de 0 a 10 seu puto')
print('Advinha vagabundo')
acertou = False
while not acertou:
    jog = int(input('Advinhe o numero:'))
    tentativas += 1
    if jog == computador:
        acertou =True
        print('Acertou Miseravel levou {} tentativas'.format(tentativas))
    elif jog != computador:
        acertou = False
        print('Errou imbecil tenta de novo')
