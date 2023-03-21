cont = 0
soma = 0
for c in range(1, 7):
    num = int(input('Digite o {} numero'.format(c)))
    if num % 2 ==0:
        soma += num
        cont+= 1
print('você informou {} numeros pares e a soma foi {}'.format(cont,soma))



    #se o pedido de um valor for posto dentro de um laço for ele se reptira x vezes
    # sendo X o rangue do for.