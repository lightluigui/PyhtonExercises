nome = str(input('Digite seu nome:')).lower()
if nome == 'matheus':
    print('Que nome lindo')
else:
    print('toma no cu nome feio')
print('Bom dia {}'.format(nome))

n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
media = (n1+n2)/2
print('A sua media foi {:.1f} '.format(media))
if media >=6:
    print('Sua nota foi boa')
else:
    print('Sua nota foi ruim estude mais')

#pra saber oq esta dentro do if ou else é so olhar a identaçao