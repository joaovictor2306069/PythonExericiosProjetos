import random
n1 = str(input('Primeiro nome: '))
n2 = str(input('Segundo  nome: '))
n3 = str(input('Terceiro  nome: '))
n4 = str(input('Quarto  nome: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))
num_usuario = input('Escolha um número de 0 a 100: ')
#escolhe um numero entre 0 e 100
num_sorteado = random.randint(0, 100)
if num_usuario == num_sorteado:
    print('Parabéns, você acertou!')
else:
    print('Você errou! O número sorteado foi:', num_sorteado)
