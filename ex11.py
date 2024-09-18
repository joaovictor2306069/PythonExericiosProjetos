velocidade = float(input('Por favor, informe sua velocidade em Km/hora: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Voce ultrapassou o limite da via que é de 80Km/h, sua multa será no valor de {} R$'.format(multa))
else:
    print('Tenha um bom dia, dirija com cuidado sempre!')


