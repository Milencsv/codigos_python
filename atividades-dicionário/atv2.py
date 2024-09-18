# Palavras que estarão no dicionário
palavras = {
     "apple": "maçã", "dog": "cachorro", "cat": "gato", "car": "carro", "book": "livro", "house": "casa", "school": "escola", "water": "água", "computer": "computador", "phone": "telefone", "sun": "sol", "moon": "lua", "tree": "árvore", "flower": "flor", "bread": "pão", "milk": "leite", "bird": "pássaro", "pen": "caneta", "shoe": "sapato", "chair": "cadeira"
}

# A função irá receber uma palavra em inglês e retornar sua versão em português
def tradutor(palavra_ingles):
    if palavra_ingles in palavras:
        return f"A tradução de {palavra_ingles} é {palavras[palavra_ingles]}"
    else:
        print("Essa palavra desejadanão existe")
# Pede uma palavra ao usuário para traduzir
palavra = input("Digite uma palavra em inglês para ver sua tradução: ")

# Chama a função e exibe o resultado
print(tradutor(palavra))