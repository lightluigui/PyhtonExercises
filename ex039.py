num = int(input('Digite um numero inteiro:'))
print('''Escolha uma das bases para coverçao:
[ 1 ] BINARIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL''')
opt = int(input('Sua opcão:'))
if opt == 1:
    print('{} convertido para binario é {}'.format(num,bin(num)[2:]))
elif opt == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opt == 3:
    print('{} convertido para hexadecima é {}'.format(num,hex(num)[2:]))
else:
    print('Opcão invalida tente novamente')

# bin é uma funçao do python que transforma em binario
# oct é uma funçao que transforma em octal
# hex é uma funçao que transforma em hexadecimal