nome = str(input('Digite seu nome e sobrenome: ')).strip()
print('muito prazer em te conhecer {}'.format(nome))
n = nome.split()
print('Seu primeiro nome é {}'. format(n[0]))
print('Seu ultimo nome é {}'. format(n[len(n)-1]))
print('Verificando se o seu nome contem a palavra Pereria.. {}'.format('PEREIRA' in nome.upper()))
frase = str(input('Digite uma frase: ')).strip().upper()
print('Analisando...A letra A apareceu {} vezes.'.format(frase.count('A')))
print('A primeira letra A encontrada na frase foi na posição {}'.format(frase.find('A')+1))
print('A ultima letra A é encontrado na frase foi na posição {}'.format(frase.rfind('A')+1))




