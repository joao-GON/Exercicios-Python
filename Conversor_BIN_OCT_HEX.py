#### Conversor de bases binária, octal e hexadecimal
 
#Pergunta o numero

numero= (int(input("Digite seu número: ")))
print("informe a base de conversão: \n [1- Binário]\n [2- Octal]\n [3-Hexadecimal] ")
opcao = int(input("Sua opção: "))

#Filtro condicional de opção

#Binário
if opcao == 1:
    binario = "{0:b}".format(numero)
    print ("{} convertido em binário é igual a: {}".format(numero,binario))

#Octal
elif opcao== 2:
      octal = "{0:o}".format(numero)
      print ("{} convertido em octal é  igual a: {}".format(numero,octal))

#Hexadecimal
else :
    opcao== 3
    hexa = "{0:x}".format(numero)
    print ("{} convertido em Hexadecimal é  igual a: {}".format(numero,hexa))

    

############## A N O T A Ç Õ E S   D E   E S T U D O S {0:b}".format(valorqualquer)

## 1. numero = {x}: Aqui estamos definindo uma variável numero e atribuindo a ela o valor {x}. Este é o número que queremos converter para binário.

## 2. binario = "{0:b}".format(numero): Nesta linha, estamos convertendo o número para binário. Usamos a função format() para formatar a string "{0:b}",
## onde {0} é um marcador de posição que será substituído pelo valor da variável numero, e :b indica que queremos a representação binária desse número. 
## Isso converte numero em binário e armazena o resultado na variável binario.

## 3. print("{} convertido em binário é igual a: {}".format(numero, binario)): Aqui estamos usando o método .format() para criar uma string formatada
## que exibe o número original e sua representação em binário. "{} e {} são marcadores de posição que serão substituídos pelos valores de numero e binario, respectivamente. 
## Esta string formatada é então passada para a função print(), que a imprime no console.

## Esta explicação é exatamente a mesma para Octal(o) e Hexadecimal(x) e claro Binário (b).##



