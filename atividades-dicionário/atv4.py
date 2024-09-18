itens_vendidos = {}

for contador in range (1,9):
    produto = input(f"Digite o nome do produto {contador}: ")
    quantidade_vendida = input(f"Quantas unidades de {produto} foram vendidas?: ")
    itens_vendidos[produto] = quantidade_vendida
def atualiza_itens(produto,quantidade_vendida):
    