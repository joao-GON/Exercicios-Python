
##Mensagem
print("insira 2 números para saber qual é o maior, o menor e ou se são iguais")

##Insere Valores

A= int(input("Digite o primeiro número: "))
B= int(input("Digite o segundo número: "))

if A > B:
    print(A," é maior que ",B, "e",B,"menor que",A)

elif B > A:
    print(B," é maior que ",A, "e",A,"menor que",B)

else:
    A == B
    print(A,"É igual a",B)
