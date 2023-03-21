somaidade =0
mediaidade =0
maioridadehomem = 0
nomevelho = ''
nummulheres = 0
for p in range(1,5):
    print('----{}ª Pessoa -----'.format(p))
    nome= str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo[M/F]:')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem =idade
        nomevelho = nome
    if idade < 20 and sexo in'Ff':
        nummulheres += 1

mediaidade = somaidade/4
print('a media da idade do grupo é {} anos'.format(mediaidade))
print('o homem mais velho se chama {} e tem {} anos'.format(nomevelho,maioridadehomem))
print('{} mulheres tem menos de 20 anos'.format(nummulheres))