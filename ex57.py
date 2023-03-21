n1 = int(input('Digite um numero:'))
n2 = int(input('digite outro numero:'))
print('     [1] Somar')
print('     [2] Multiplicar')
print('     [3] Maior')
print('     [4] novos numeros')
print('     [5] Sair')
opt = int(input('>>>>> Qual sua opcão?'))
while opt == 1:
    soma = n1+n2
    print(' a soma de {} e {} é igual a {}'.format(n1,n2,soma))
    break
while opt == 2:
        mult = n1 * n2
        print(' a multiplicaçao de {} e {} é igual a {}'.format(n1, n2, mult))
        break
while opt == 3:
           if n1 > n2:
               print('o maior numero é {}'.format(n1))
           if n2 > n1:
               print('o maior numero é {}'.format(n2))
           break
while opt == 4:
    n1 = int(input('Digite um numero:'))
    n2 = int(input('digite outro numero:'))
    print('os novos numeros sao {} e {}'.format(n1,n2))
    break
while opt == 5:
    print('fim do programa obrigado')
    break