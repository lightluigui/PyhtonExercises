pre = float(input('digite o preço do ´produto R$:'))
des = pre - (pre * 5 / 100)
print('o preço do produto {} vai ficar {:.1f} com 5% de desconto'.format(pre, des))

