a = float(input('Informe um número: '))
b = float(input('Informe um número: '))
c = float(input('Informe um número: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor escolhido foi {}'.format(menor))
print('O maior valor escolhido foi {}'.format(maior))


