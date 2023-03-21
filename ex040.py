n1 = float(input('Digite o primeiro numero:'))
n2 = float(input('Digite o segundo numero:'))
if n1>n2:
    print('\033[31m o primeiro é maior')
elif n1<n2:
    print('\033[32m o segundo é maior\033[m')
elif n1 ==n2:
    print('\033[33m sao iguais')