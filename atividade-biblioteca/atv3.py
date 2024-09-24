def exibir_menu():
    print("\nMenu de Gerenciamento de Eventos")
    print("1. Adicionar um novo evento")
    print("2. Remover um evento")
    print("3. Sair")
    opcao = int(input("\nEscolha uma opção (1-3): "))
    return opcao

def exibir_eventos(eventos):
    if eventos:
        print("\nEventos agendados:")
        for i, evento in enumerate(eventos, 1):
            print(f"{i}. {evento}")
    else:
        print("\nNenhum evento agendado.")

def adicionar_evento(eventos):
    novo_evento = input("\nDigite o nome do novo evento: ")
    eventos.append(novo_evento)
    print(f"\nEvento '{novo_evento}' adicionado com sucesso!")

def remover_evento(eventos):
    if not eventos:
        print("\nNão há eventos para remover.")
        return
    exibir_eventos(eventos)
    posicao = int(input("\nQual a posição do evento a remover? "))
    if 1 <= posicao <= len(eventos):
        evento_removido = eventos.pop(posicao - 1)
        print(f"\nEvento '{evento_removido}' removido com sucesso!")
    else:
        print("\nPosição inválida.")

def main():
    eventos = ["Reunião com a equipe", "Almoço com cliente", "Consulta médica"]
    
    while True:
        exibir_eventos(eventos)
        opcao = exibir_menu()

        if opcao == 1:
            adicionar_evento(eventos)
        elif opcao == 2:
            remover_evento(eventos)
        elif opcao == 3:
            print("\nSaindo do programa...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

# Executa o programa
main()
