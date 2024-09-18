nome = str(input('Digite seu nome e sobrenome: ')).strip()
print('Analisando seu nome, aguarde...')
print('Seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome)- nome.count(' ')))
num = int(input('Digite o valor de número: '))
print('Analisando, aguarde...'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O valor númerico solicitado possui {} de unidades.'.format(u))
print('O valor númerico solicitado possui {} de dezenas.'.format(d))
print('O valor númerico solicitado possui {} de centenas.'.format(c))
print('O valor númerico solicitado possui {} de milhares.'.format(m))
