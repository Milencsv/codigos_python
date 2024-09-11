media = 33.5
acima_ou_igual = 0
abaixo = 0

for contador in range(7):
    temperatura = float(input(f"Digite a temperatura {contador + 1}: "))
    
    if temperatura >= media:
        acima_ou_igual += 1
    else:
        abaixo += 1


print(f"Temperaturas iguais ou acima da média (33.5): {acima_ou_igual}")
print(f"Temperaturas abaixo da média (33.5): {abaixo}")
