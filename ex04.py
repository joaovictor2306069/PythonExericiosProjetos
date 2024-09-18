import math
a = float(input('Digite o valor do cateto adjacente: '))
o = float(input('Digite o valor do cato oposto: '))
Hip = math.hypot(a,o)
print('O valor da hipotenusa é de {:.2f} unidades de área'.format(Hip))
angulo = float(input('Digite o valor do angulo que voce deseja converter: '))
seno = math.sin(math.radians(angulo))
cose = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O valor de seno: {:.2f}'.format(seno))
print('O valor de cosseno : {:.2f}'.format(cose))
print('O valor da tangente: {:.2f}'.format(tang))

