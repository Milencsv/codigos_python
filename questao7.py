# Função para calcular o valor final com base na condição de pagamento
def calcular_valor_final(preco, codigo_pagamento):
    if codigo_pagamento == 1:
        # Pix, dinheiro ou débito: 15% de desconto
        valor_final = preco * 0.85
    elif codigo_pagamento == 2:
        # À vista no cartão de crédito: 10% de desconto
        valor_final = preco * 0.90
    elif codigo_pagamento == 3:
        # Em duas vezes: preço normal sem juros
        valor_final = preco
    elif codigo_pagamento == 4:
        # Em três vezes: preço normal + 10% de juros
        valor_final = preco * 1.10
    else:
        # Caso código inválido
        return "Código de pagamento inválido"

    return valor_final

# Entrada de dados
preco = float(input("\nDigite o preço do produto: R$ "))
codigo_pagamento = int(input("\nPix, dinheiro ou débito: 15% de desconto(1);\nÀ vista no cartão de crédito: 10% de desconto(2);\nEm duas vezes: preço normal sem juros(3);\nEm três vezes: preço normal + 10% de juros(4).\n\nDigite o código da condição de pagamento: "))

# Cálculo do valor final
valor_final = calcular_valor_final(preco, codigo_pagamento)

# Saída dos resultados
if isinstance(valor_final, str):
    print(valor_final)
else:
    print(f"\nValor original: R$ {preco:.2f}\n")
    print(f"Código de pagamento escolhido: {codigo_pagamento}\n")
    print(f"Valor final: R$ {valor_final:.2f}\n")