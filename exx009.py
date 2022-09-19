medida=float(input("valor em metros:"))
km=medida/1000
cm= medida * 100
mm=medida*1000
print('a medida de {:.1f} em metros, equivale a: \n{} quilometros \n{} centimetros \n{} milimetros'.format(medida,km,cm,mm))