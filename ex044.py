peso = float(input('Digite seu peso (kg):'))
altura = float(input('Digite sua altura (m):'))
imc = peso / (altura ** 2)
if imc >=13 and imc <25:
    print('esta em seu peso ideal')
elif imc > 25 and imc<30:
    print('esta com sobrepeso')
elif imc >30:
    print('Voce esta obeso')
elif imc <13:
    print('voce esta abaixo de seu peso ideal')

print('seu imc é {:.1f}'.format(imc))
