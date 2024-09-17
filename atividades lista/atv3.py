numeros = []
for i in range(6):
    numero = float(input(f"Digite um número {i+1}: "))
    numeros.append(numero)
print("\nLista de Números:", numeros)

esc1 = int(input("Escolha a primeira posição que você deseja: "))
esc2 = int(input("Escolha a segunda posição que você deseja: "))

num1 = numeros[esc1]
num2 = numeros[esc2]

produto = num1 * num2
soma = num1 + num2
diferenca = num1 - num2
divisao = num1 / num2 if num2 != 0 else "Divisão por zero não permitida"
exponenciacao = num1 ** num2

# Exibe os resultados
print(f"\nProduto: {produto}")
print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Divisão: {divisao}")
print(f"Exponenciação: {exponenciacao}")