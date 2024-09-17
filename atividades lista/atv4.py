
lista = [int(input(f"Digite o {i+1}º número: ")) 
    for i in range(10)]

posicao = []
i = 0

for valor in lista:
    if valor == 3:
        posicao.append(i)
    i += 1

if posicao:
    print("O número 3 foi encontrado nas posições: {}".format(posicao))
else:
    print("O número 3 não foi encontrado na lista.")