
Carro = float(input("Qual a velocidade do carro? "))
Multa= 0

if Carro > 80 :
    Multa += (Carro-80)* 7
    print("Você ultrapassou a velocidade permitida (80KM/H),sua multa é de R$:", Multa)
else:
    print("Você está dentro do limite de velocidde, boa viagem! :)")