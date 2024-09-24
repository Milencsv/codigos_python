def ler_lista(mensagem):
    # Função para ler uma lista de números inteiros fornecida pelo usuário, manualmente
    print(mensagem)
    lista = []
    numero = ""
    caractere = input()  # Recebe uma string do usuário

    for c in caractere:
        if c != " ":  # Se não for um espaço, faz parte do número
            numero += c
        elif c == " " and numero != "":  # Separador de números
            lista.append(int(numero))  # Adiciona o número à lista
            numero = ""  # Reseta o número para o próximo
    if numero != "":  # Adiciona o último número, caso tenha sobrado
        lista.append(int(numero))

    return lista

def intersecao_listas(lista1, lista2):
    # Função para encontrar a interseção entre duas listas sem usar conjuntos
    intersecao = []
    
    for num1 in lista1:
        for num2 in lista2:
            if num1 == num2 and num1 not in intersecao:
                intersecao.append(num1)

    # Ordena a interseção sem usar len() e sem try/except
    i = 0
    while True:
        if i >= len(intersecao):  # Para a ordenação, precisa verificar se i é menor que o comprimento da lista
            break
        j = i + 1
        while True:
            if j >= len(intersecao):  # Verifica se j é menor que o comprimento da lista
                break
            if intersecao[i] > intersecao[j]:
                intersecao[i], intersecao[j] = intersecao[j], intersecao[i]
            j += 1
        i += 1

    return intersecao

def main():
    # Lê duas listas de números inteiros fornecidas pelo usuário
    lista1 = ler_lista("Digite os números da primeira lista separados por espaço: ")
    lista2 = ler_lista("Digite os números da segunda lista separados por espaço: ")

    # Encontra a interseção entre as duas listas
    intersecao = intersecao_listas(lista1, lista2)

    # Exibe o resultado
    if intersecao:
        print("Números comuns (em ordem crescente):", intersecao)
    else:
        print("Não há números comuns entre as listas.")

# Executa o programa principal
if __name__ == "__main__":
    main()
