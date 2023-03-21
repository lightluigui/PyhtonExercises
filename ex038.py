casa = float(input('Valor da casa:'))
salario = float(input('Salario do comprador:'))
pres = float(input('Quantos anos de finaciamento:'))
calculo = casa/(pres*12)
limite = salario/100 * 30
print('uma casa de {} em {:.0f} tera prestaçoes e {:.2f} '.format(casa,pres,calculo))
if calculo>salario:
    print('Emprestimo negado sinto muito')
elif calculo > limite:
    print('Emprestimo negado sinto muito')
else:
    print('Emprestimo aprovado')



















#pode ter apenas 1 else
#nao se pode usar elif sem if
#elif é a mesma coisa de else if de outras linguagens