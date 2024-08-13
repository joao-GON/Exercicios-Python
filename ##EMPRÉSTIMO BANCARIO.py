20##EMPRÉSTIMO BANCARIO 

## Pergunta o valor do empéstimo
emprestimo = int(input("Qual o valor do empréstimo? "))
print(emprestimo)
## Pergunta o salário
salario = int(input("Qual o valor do seu salário? "))
print(salario)
## Pergunta quantos anos
anos = int(input("em quantos anos você pretendo pagar? "))
print(anos)
##Calcular valor da prestação sem poder exceder 30% do salário 
valor_limite_salario= salario * 0.3
print("Valor limite da parcela considerando seu salário (Não exedendo 30% do mesmo)= ",valor_limite_salario)
## Prestação é o valor mensal do empréstimo dividisdo pelos anos
prestacao = emprestimo / (anos *12)
print("Valor da Prestação",prestacao)
print("")
if prestacao < valor_limite_salario:
    print ("Empréstimo Aprovado ! Salario",{salario}, " condiz para a prestação",{prestacao}, " do Empréstimo,com valor limite de" ,{valor_limite_salario},"!")

elif prestacao >  valor_limite_salario:
    print ("Empréstimo negado! Salario insuficiente para o Empréstimo!")
