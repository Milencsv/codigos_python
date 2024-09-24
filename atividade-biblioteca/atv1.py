def ler_lista():
    # Lê uma lista de números inteiros fornecida pelo usuário
    return list(map(int, input("Digite os números da lista separados por espaço: ").split()))

def intersecao(lista1, lista2):
    # Encontra os elementos comuns entre duas listas
    comum = []
    for num in lista1:
        if num in lista2 and num not in comum:
            comum.append(num)
    return comum

def main():
    # Lê as duas listas
    print("Digite os números da primeira lista:")
    lista1 = ler_lista()
    print("Digite os números da segunda lista:")
    lista2 = ler_lista()
    
    # Encontra a interseção
    comuns = intersecao(lista1, lista2)
    
    # Exibe a lista de números comuns em ordem crescente
    if comuns:
        comuns.sort()  # Ordena os números comuns em ordem crescente
        print("Números comuns em ambas as listas:", comuns)
    else:
        print("Não há números comuns entre as listas.")

# Executa o programa
main()
