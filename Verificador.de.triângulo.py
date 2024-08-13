##Verificador de triângulo

print("Entre com os valores das retas para verificar se o triângulo é possível: ")

A = float(input("Entre com a valor da primeira reta "))
B = float(input("Entre com a valor da segunda reta "))
C = float(input("Entre com a valor da terceira reta "))

if (A + B > C) and (A + C > B) and (B + C > A):
    print("O triângulo pode ser formado")
else:
    print("O triângulo não pode ser formado")

