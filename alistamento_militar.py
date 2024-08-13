
## Ficha de alistamento militar

ano_ad= 2006

#Recolhe ano de nascimento
print("Ficha de alistamento militar" )
print(" ")
ano_nascimento = (int(input("Insira seu ano nascimento: ")))

if ano_nascimento == ano_ad:
    print(" Você deve se alistar esse ano")

elif ano_nascimento < ano_ad: 
    print(" Você já passou do prazo, aliste-se o mais rápido possível")

else:
    if ano_nascimento > ano_ad :
       print(" Você ainda não deve se alistar")
