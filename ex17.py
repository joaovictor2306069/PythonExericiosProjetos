import math
triangulo_a = float(input('Informe o valor do primeiro segmento: '))
triangulo_b = float(input('Informe o valor do segundo segmento: '))
triangulo_c = float(input('Informe o valor do terceiro segmento: '))
print('Analisando e verificando se é possivel formar um triangulo com essas medidias..')
if triangulo_a < triangulo_b + triangulo_c and triangulo_b < triangulo_a + triangulo_c and triangulo_c < triangulo_a + triangulo_b:
    print('Os segmentos podem formar um triangulo.')
else:
    print('Os segmentos fornecidos não podem formar um triangulo.')

