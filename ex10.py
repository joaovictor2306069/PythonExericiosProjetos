import random
computador = random.randint (0,5)
print('Pensei em um número entre 0 a 5..Tente advinhar em que número eu pensei? HAHAHA')
jogador = int(input('Escolha um número de 0 a 5 my lord: '))
if jogador == computador:
     print('Parabens !! Você acertou')
else:
    print('Voce errou, Tente na proxima HAHAAH')
    
