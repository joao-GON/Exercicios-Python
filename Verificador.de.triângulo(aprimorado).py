## analisador de triangulo

triangulo = 0

## Entra com os valores
print("Entre com os valores das retas para verificar se o triângulo é possível: ")

A = float(input("Entre com a valor da primeira reta "))
B = float(input("Entre com a valor da segunda reta "))
C = float(input("Entre com a valor da terceira reta "))

##Testa se pode ser formado
if (A + B > C) and (A + C > B) and (B + C > A):
    print("O triângulo pode ser formado")
    triangulo = True

    ##Pode ser formado
    while triangulo == True: 
    ## T. EQUI = LADOS IGUAIS
        if A == B == C: 
         print("Triangulo Equilátero, todos os lados são iguais")
         break
    ## T. ESCA = TODOS LADOS DIFERENTES
        elif (A != B) and (A != C) and (B != C):
         print ("Triângulo esacaleno, todos os lados são diferentes")
         break
    ## T. ISÓS = DOIS LADOS IGUAIS
        elif (A!= B and (A==C or B==C)) or (A!=C and (A==B or B==C )) or (B!=C and (A==B or C==A)):
         print ("Trângulo isóceles, Possui dois lados iguais")
         break

    print ("")

##Não pode ser formado
else:
    print("O triângulo não pode ser formado")
    triangulo = False

