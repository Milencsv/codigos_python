maiores_de_idade = 0

for contador in range(5):
    idade = int(input(f"Digite a idade da {contador + 1} pessoa: "))

    if idade >= 18:
        maiores_de_idade += 1

print(f"A quantidade de pessoas que possuem 18 ou +18 é a seguinte: {maiores_de_idade}")