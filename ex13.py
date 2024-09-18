viagem = float(input('Por favor, informe a distânica total percorrida em KM de sua viagem: '))
viagem_menor = (viagem * 0.50)
viagem_maior = (viagem * 0.45)
if viagem >= 80:
   print('O valor total da sua distância percordida de {} terá um custo de {}R$'.format(viagem, viagem_menor))
else:
    print('O valor total da sua distância percordida de {} terá um custo de {}R$'.format(viagem, viagem_maior))
# também pode ser feito como : viagem = distancia * 0.50 if distancia <= 200 else distancia * 0.45
