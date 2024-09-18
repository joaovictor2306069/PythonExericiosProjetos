casa = float(input('Qual o valor do imovél que o Sr(a) deseja adquirir ? '))
salario = float(input('Informe o seu salário em reais: '))
parcelas = float(input('Informe em quantos anos você deseja financiar este imóvel: '))
print('Estamos analisando seu credito conforme seus dados. Por favor, aguarde!...')
if salario + (salario * 0.3) < casa / parcelas:
    print('\033[1;4;35;40mNão será possivel adquirir este imóvel!\033[m')
else:
    print('\033[1;4;35;40mParabéns, seu crédito foi aprovado !!\033[m')


