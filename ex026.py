frase = str(input('Digite uma frase:')).strip().upper()
print('A letra A apreceu {} vezes'.format(frase.count('A')))
print('a primeira letra A apreceu na posiçao {}'.format(frase.find('A')))
print(' a ultima letra A apreceu na posiçao {}'.format(frase.rfind('A')))
#rfind encontra a letra contando do direita pra esquerda
