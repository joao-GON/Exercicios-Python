
## GERENCIAMENTO DE PAGAMENTOS

## CRIAR O INPUT PAGAMENTO (EX: 1000 R$)
pagamento = int (input("Digite o valor do seu produto pra saber o valor do desconto: R$ "))
print("")
##VERIFICAR O MÉTODO (1,2,3,4)
metodo_pag  = int(input("Digite:\n [1]- Para pagar a vista em  dinehiro\n [2]- Para pagar a vista no cartão\n [3]- Para parcelar em 2x no cartão\n [4]- Para parcelar em 3x ou mais no cartão\n : "))
##CRIA ESTRUTURAS DE CONTROLE PARA VERIFICAR O MÉTODO (1,2,3,4)

if metodo_pag == 1:
    desconto_1 = pagamento - (pagamento * 0.1)
    print("O preço que você irá pagar é de R$ {:.2f}".format(desconto_1).replace('.', ','))

elif metodo_pag == 2:
    desconto_2 = pagamento - (pagamento *0.05)
    print("O preço que você irá pagar é de R$ {:.2f}".format(desconto_2).replace('.',','))

elif metodo_pag == 3: 
    parcelamento = pagamento/2 
    print("Você pagará 2 parcelas de R$ {:.2f} ".format(parcelamento).replace('.',','))

else: 
    if metodo_pag ==4:
     meses = int(input("Em quantos meses você pretende parcelar? "))
    if meses >= 3:
     juros = pagamento + (pagamento * 0.2) 
     parcela = juros/3
     print("O preço que você irá pagar com juros de 20% são  de R$ {:.2f}".format(juros).replace('.',','), "Em parcelas de R$ {:.2f}".format(parcela).replace('.',','))
    else: 
       TypeError = True 
       print("*ERRO* (_Insira um mês válido maior que 3_)")




############## A N O T A Ç Õ E S   D E   E S T U D O S {:.2f}

##{}: Isso é como um espaço reservado em uma frase. Quando você usa {}, está dizendo ao Python: "Coloque um valor aqui".
##":": Este sinal indica que você está prestes a dar instruções de formatação ao Python.
##.2: Isso significa que você quer que o número tenha duas casas decimais após o ponto decimal.
##f: Isso indica que você está formatando um número de ponto flutuante (um número decimal).
##Então, quando você usa "{:.2f}", está basicamente dizendo: "Quero inserir um número aqui e quero que ele tenha duas casas decimais". 
##Por exemplo, se o número for 10, ele será exibido como 10.00; se for 3.14159, será exibido como 3.14.


