num = int(input('Digite um numero:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[31m', end=' ')
        tot +=1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c) , end=' ')
print('\n\033[m o numero {} foi divisivel {} vezes'.format(num, tot))
if tot == 2:
    print('Ele é primo')
else:
    print('não é primo')

    #esse tot é pra armazenar a quantidade de vezes que um numero foi divido
