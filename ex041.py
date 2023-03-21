from datetime import date
nasc = int(input('Digite o ano que você nasceu:'))
atual = date.today().year
idade = atual - nasc
dif = 18 - idade
print('quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Esta na hora de se alistar.')
elif idade <18:
    print('Ainda não esta na hora de sofrer.')
    print('ainda faltam {} para seus 18 anos'.format(dif))
elif idade > 18:
    print('Ja passou da hora, cuidado pra não ser preso.')