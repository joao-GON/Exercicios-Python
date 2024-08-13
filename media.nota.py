
##Calculadora de média

print("Calculadora de média")
print("")
print("Critérios:\n Média > 7 ou maior- aprovação\n","Média < 5-Reprovação\n","Média entre 5 e 6.9- recuperação\n")
print("")

##Recolhe as notas
nota_a= (float(input("Insira a nota da primeira avaliação: ")))
nota_b= (float(input("Insira a nota da segunda avaliação: ")))

#Calcula média
media= ((nota_a+ nota_b)/2)

if media < 5: 
    print("Aluno REPROVADO")

elif media == 5 or media < 7:
    print("Aluno de RECUPERAÇÃO")

else :
    if media >= 7:
       print("Aluno APROVADO")

print("Sua média foi de:",media)

    
