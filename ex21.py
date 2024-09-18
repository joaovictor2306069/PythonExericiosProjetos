nome_aluno = str(input('Digite seu nome completo: '))
nota1 = float(input('Digite a nota que {} tirou na primeira prova: '.format(nome_aluno)))
nota2 = float(input('Digite a nota que {} tirou na segunda prova: '.format(nome_aluno)))
média = (nota1 + nota2) / 2
if média < 5.0:
    print('Você está reprovado, sua média final foi de {}'.format(média))

elif 5 <= média < 6.9:
    print('Você está de recuperação, sua média final foi de {}'.format(média))

elif média > 7:
    print('Parabéns você está aprovado,sua média final foi de {}'.format(média))
