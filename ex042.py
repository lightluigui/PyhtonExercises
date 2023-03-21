nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
media = (nota1+nota2)/2
if media>=7:
    print('\033[32m APROVADO com media {}'.format(media))
elif media<5:
    print('\033[31m REPROVADO com media {}'.format(media))
elif media >=5 and media<7:
    print('\033[33m EM RECUPERAÇÃO com media {}'.format(media))
