import math

an = float(input('digite o angulo: '))
seno = math.sin(math.radians(an))
print('o angulo de {} tem Seno {:.2f}'.format(an,seno))
coss = math.cos(math.radians(an))
print('o angulo de {} tem cosseno {:.2f}'.format(an,coss))
tan = math.tan(math.radians(an))
print('o angulo de {} tem a tangente de  {:.2f}'.format(an,tan))

#radians converte o numero para radiano
#sin calcula o seno
#cos calcula o cosseno
#tan mostra a tangente