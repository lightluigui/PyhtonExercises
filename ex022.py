nome = input('Digite seu Nome: ').strip()
dividido = nome.split()
print('Analisando seu nome...')
print('seu nome em maiusculas é {}'.format((nome.upper())))
print('seu nome em minusculas é {}'.format((nome.lower())))
print('Seu nome tem um total de {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))


#o nome.find(' ') ele contando as letras ate achar o primeiro espaço a partir do 0 assim descobre quantas letras tem
