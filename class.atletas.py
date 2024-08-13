
## Classificação de atletas 

ano_base = 2024

ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano_base - ano_nascimento

if idade <= 9 :
    print ("Atleta mirin")

elif idade <= 14:
    print("Infantil")

elif idade <= 19:
    print("júnior")

elif idade == 20:
    print("sênior")

else:
    print("Master")