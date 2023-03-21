from datetime import date
ano = int(input('Digite o ano de nascimento:'))
idade = date.today().year - ano
print('O atleta tem {} anos de idade'.format(idade))
if idade ==18 and idade >14 :
    print('Classificaçao:JUNIOR')
elif idade>18 and idade<30:
    print('Classificaçao: ADULTO')
elif idade >= 9 and idade < 14:
    print('Classificaçao:INFANTIL')
else:
    print('Provavelmente aposentado')