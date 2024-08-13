
Salário = (float(input("Insira seu salário e descubra seu aumento ")))

if Salário > 1250:
    Salário_aumento = Salário + (Salário * 0.1) 
    print ("Seu salário atual (com aumento de 10%) é ",Salário_aumento,"R$")

elif Salário <= 1250:
     Salário_aumento = Salário + (Salário * 0.15) 
     print ("Seu salário atual (com aumento de 15%) é ",Salário_aumento,"R$") 