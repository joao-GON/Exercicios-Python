
distancia = (int(input("Digite a distância da viagem (EM KM) ")))

preco_passagem=0

if distancia < 200:
    preco_passagem += distancia* 0.5
else:
    preco_passagem =+ distancia* 0.45

print ("O preço da sua passagem é: R$",preco_passagem)