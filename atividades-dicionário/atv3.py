preco_produtos={}

for contador  in range (1,5):
    nome = input(f"Digite o nome do produto {contador}: ")
    preco = float(input(f"Informe o preço do {nome}: R$"))
    preco_produtos[nome]= preco

nome_produto = input("Digite o nome do produto que procura para ver seu preço: ")

if nome_produto in preco_produtos:
    print(f"O valor de {nome_produto} é R${preco_produtos[nome_produto]}")
else:
    print("Esse produto é inexistente")