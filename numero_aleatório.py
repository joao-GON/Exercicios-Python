
import random

def escolher_numero_aleatorio():
    # Gerar uma lista de números aleatórios
    numeros = [random.randint(0, 5) for _ in range(1)]  # Gera 10 números aleatórios entre 1 e 100
    
    # Escolher um número aleatório da lista
    numero_escolhido = random.choice(numeros)
    
    return numero_escolhido

# Chamando a função para obter o número escolhido
numero = escolher_numero_aleatorio()

numero_usuario = (eval(input("Digite seu número entre 0 e 5: ")))

if numero == numero_usuario:
    print("O número escolhido pela máquina é:", numero, "Você venceu,parabéns!")
else:
    if numero != numero_usuario:
        print("O número escolhido pela máquina é:", numero, "Você perdeu!")  