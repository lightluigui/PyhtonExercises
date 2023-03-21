nome = str(input('digite seu nome:')).split()
print('seu primeiro nome é {}'.format(nome[0]))
print('seu ultimo nome é {}'.format(nome[len(nome)-1]))
#pra descobrir o ultimo nome usamos o len dentro de [] pra que len(nome)seja a posiçao que ele vai ver
#o -1 é pq como começa acontar do 0 o -1 é pra garantir o fucionamento