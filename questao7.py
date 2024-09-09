# Função para calcular o valor final com base na condição de pagamento
def calcular_valor_final(preco, codigo_pagamento):
    if codigo_pagamento == 1:
        # Pix, dinheiro ou débito: 15% de desconto
        valor_final = preco * 0.85
        parcelas = 1
        valor_parcela = valor_final
    elif codigo_pagamento == 2:
        # À vista no cartão de crédito: 10% de desconto
        valor_final = preco * 0.90
        parcelas = 1
        valor_parcela = valor_final
    elif codigo_pagamento == 3:
        # Em duas vezes: preço normal sem juros
        valor_final = preco
        parcelas = 2
        valor_parcela = valor_final / parcelas
    elif codigo_pagamento == 4:
        # Em três vezes: preço normal + 10% de juros
        valor_final = preco * 1.10
        parcelas = 3
        valor_parcela = valor_final / parcelas
    else:
        return "Código de pagamento inválido"

    return valor_final, parcelas, valor_parcela

# Entrada de dados
preco = float(input("\nDigite o preço do produto: R$ "))
codigo_pagamento = int(input("\nPix, dinheiro ou débito: 15% de desconto(1);\nÀ vista no cartão de crédito: 10% de desconto(2);\nEm duas vezes: preço normal sem juros(3);\nEm três vezes: preço normal + 10% de juros(4).\n\nDigite o código da condição de pagamento: "))

# Cálculo do valor final
resultado = calcular_valor_final(preco, codigo_pagamento)

# Saída dos resultados
if isinstance(resultado, str):
    print(resultado)
else:
    valor_final, parcelas, valor_parcela = resultado,
    print(f"\nValor original: R$ {preco:.2f}")
    print(f"\nCódigo de pagamento escolhido: {codigo_pagamento}")
    print(f"\nValor final: R$ {valor_final:.2f}")
    
    if parcelas > 1:
        print(f"\nNúmero de parcelas: {parcelas}")
        print(f"\nValor de cada parcela: R$ {valor_parcela:.2f}")
