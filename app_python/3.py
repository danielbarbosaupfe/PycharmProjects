a = int (input("Digite um numero"))
div = 0
x=0

for x range(1, a+1):
	resto = a % x
	if resto == 0:
	div = div +1

if div ==2:
  print('numero:{} é primo'.format(a))
else:
  print('numero:{} nao é primo'.format(a))
