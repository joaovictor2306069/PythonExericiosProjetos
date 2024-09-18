nome = str(input('Escreva seu nome completo: ')).strip()
idade = float(input('Informe a sua idade: '))
alistamento = 17 < idade < 18
if idade < 18:
    print('\033[;1;34;40m{} , não será necessario seu alistamento este ano,porém, no proximo ano procure uma junta militar para realizar seu alistamento\033[m'.format(nome))
elif idade == 18:
    print('\033[;1;34;40m{} procure uma junta militar! Você deverá realizar o alistamento.\033[m'.format(nome))
else:
    print('\033[;1;34;40m{} seu alistamento está atrasado, procure uma junta militar mais próxima!\033[m'.format(nome))

