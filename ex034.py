from datetime import date
ano = int(input('Qual ano quer analisar? Digite 0 para o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('o ano de {} É Bissexto'.format(ano))
else:
    print('o ano atual {} Nao é Bissexto'.format(ano))




# date ta sendo usado para pegar a informaçao do ano que esta no pc
 #se o ano for divisivel por 4 nao divisivel por 100 e divisivel por 400 ele é bissexto
