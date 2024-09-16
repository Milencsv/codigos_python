import random

numero_secreto = random.randint(1, 100)

tentativas_restantes = 5

print("Bem-vindo ao jogo da adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")

while tentativas_restantes > 0:

    palpite = int(input("Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns! Você acertou o número!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")

    tentativas_restantes -= 1
    
    if tentativas_restantes > 0:
        print(f"Você ainda tem {tentativas_restantes} tentativas.")
    else:
        print(f"Suas tentativas acabaram. O número secreto era {numero_secreto}.")